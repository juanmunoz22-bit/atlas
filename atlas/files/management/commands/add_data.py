from django.core.management.base import BaseCommand
import pandas as pd
from files.models import File_Header
from sqlalchemy import create_engine

class Command(BaseCommand):
    help = 'Add data to the database'

    def handle(self, *args, **options):
        
        excel_file = 'ARCHIVO_EJEMPLO.xlsx'
        file_header = pd.read_excel(excel_file, sheet_name='NÓMINA', skiprows=2, nrows=1, usecols='B:D,I:J')
        file_header = file_header.rename(columns={'TIPO DOCUMENTO APORTANTE': 'tipo_documento', 'NUMERO DOCUMENTO APORTANTE': 'numero_documento', 'RAZON SOCIAL': 'razon_social', 'REFERENCIA': 'referencia', 'SOLICITUD': 'solicitud'})

        engine =create_engine('sqlite:///db.sqlite3')

        file_header.to_sql(File_Header._meta.db_table, con=engine, index=False, if_exists='append')
