from django.shortcuts import render

# Create your views here.

import pandas as pd
from files.models import File_Header
from sqlalchemy import create_engine
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    if request.method == 'GET':
        return render(request, 'file.html')
    else:
        excel_file = request.FILES['excel_file']
        file_header = pd.read_excel(excel_file, sheet_name='NÓMINA', skiprows=2, nrows=1, usecols='B:D,I:J')
        file_header = file_header.rename(columns={'TIPO DOCUMENTO APORTANTE': 'tipo_documento', 'NUMERO DOCUMENTO APORTANTE': 'numero_documento', 'RAZON SOCIAL': 'razon_social', 'REFERENCIA': 'referencia', 'SOLICITUD': 'solicitud'})

        engine =create_engine('sqlite:///db.sqlite3')

        file_header.to_sql(File_Header._meta.db_table, con=engine, index=False, if_exists='append')

        return render(request, 'file.html')