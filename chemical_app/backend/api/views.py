from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import FileResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import pandas as pd
from .models import EquipmentDataset


class UploadCSV(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        file = request.FILES.get("file")
        if not file:
            return Response({"error": "No file uploaded"}, status=400)

        df = pd.read_csv(file)

        total = len(df)
        avg_flowrate = df["Flowrate"].mean()
        avg_pressure = df["Pressure"].mean()
        avg_temperature = df["Temperature"].mean()
        type_dist = df["Type"].value_counts().to_dict()

        dataset = EquipmentDataset.objects.create(
            total=total,
            avg_flowrate=avg_flowrate,
            avg_pressure=avg_pressure,
            avg_temperature=avg_temperature,
            type_distribution=type_dist
        )

        # keep only last 5
        if EquipmentDataset.objects.count() > 5:
            EquipmentDataset.objects.first().delete()

        return Response({
            "message": "Uploaded successfully",
            "summary": {
                "total": total,
                "avg_flowrate": avg_flowrate,
                "avg_pressure": avg_pressure,
                "avg_temperature": avg_temperature,
                "type_distribution": type_dist
            }
        })


class Summary(APIView):
    def get(self, request):
        last = EquipmentDataset.objects.last()
        if not last:
            return Response({"message": "No data yet"})

        return Response({
            "total": last.total,
            "avg_flowrate": last.avg_flowrate,
            "avg_pressure": last.avg_pressure,
            "avg_temperature": last.avg_temperature,
            "type_distribution": last.type_distribution
        })


class DownloadReport(APIView):
    def get(self, request):
        last = EquipmentDataset.objects.last()
        if not last:
            return Response({"error": "No data"}, status=404)

        file_name = "report.pdf"
        c = canvas.Canvas(file_name, pagesize=letter)
        text = c.beginText(50, 750)

        text.textLine("Chemical Equipment Report")
        text.textLine("---------------------------")
        text.textLine(f"Total: {last.total}")
        text.textLine(f"Avg Flowrate: {last.avg_flowrate}")
        text.textLine(f"Avg Pressure: {last.avg_pressure}")
        text.textLine(f"Avg Temperature: {last.avg_temperature}")
        text.textLine("")

        for k, v in last.type_distribution.items():
            text.textLine(f"{k}: {v}")

        c.drawText(text)
        c.save()

        return FileResponse(open(file_name, "rb"), as_attachment=True)
