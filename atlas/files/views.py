from django.shortcuts import render

# Create your views here.

import pandas as pd
from files.models import File_Header, File_Fixed
from sqlalchemy import create_engine
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    if request.method == 'GET':
        return render(request, 'file.html')
    else:
        excel_file = request.FILES['excel_file']

        file_header = pd.read_excel(
            excel_file, 
            sheet_name='NÓMINA', 
            skiprows=2, 
            nrows=1, 
            usecols='B:D,I:J')

        file_header = file_header.rename(
            columns={
                'TIPO DOCUMENTO APORTANTE': 'tipo_documento',
                'NUMERO DOCUMENTO APORTANTE': 'numero_documento', 
                'RAZON SOCIAL': 'razon_social', 
                'REFERENCIA': 'referencia', 
                'SOLICITUD': 'solicitud'
            }
        )

        file_fixed = pd.read_excel(
            excel_file, 
            sheet_name='NÓMINA', 
            header=5, 
            usecols='B:M'
        )

        #ORDEN	TIPO DOC	NÚMERO	NOMBRE COTIZANTE	CARGO	AÑO	MES	SALARIO DIAS TRAB	DIAS INCAP	DIAS LICEN	TOTAL DIAS	F.INGRESO

        file_fixed = file_fixed.rename(
            columns={
                'ORDEN': 'orden',
                'TIPO DOC': 'tipo_documento',
                'NÚMERO': 'numero_documento',
                'NOMBRE COTIZANTE': 'nombre_cotizante',
                'CARGO': 'cargo',
                'AÑO': 'anio',
                'MES': 'mes',
                'SALARIO': 'salario',   
                'DIAS TRAB': 'dias_trab',
                'DIAS INCAP': 'dias_incap',
                'DIAS LICEN': 'dias_licen',
                'TOTAL DIAS': 'total_dias',
                'F.INGRESO': 'f_ingreso',

            }
        )


        engine = create_engine('sqlite:///db.sqlite3')

        file_header.to_sql(File_Header._meta.db_table, con=engine, index=False, if_exists='append')
        referencia = pd.read_sql('SELECT "referencia" FROM files_file_header ORDER BY id DESC LIMIT 1', con=engine)
        breakpoint()
        file_fixed['referencia_id'] = referencia['referencia']
        file_fixed.to_sql(File_Fixed._meta.db_table, con=engine, index=False, if_exists='append')

        return render(request, 'file.html')