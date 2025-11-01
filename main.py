import pandas as pd
import os
from report_generator.spendings.spendings import Spendings
from generatorLoader import GeneratorLoader
from core.arguments import Arguments
from core.report_name_mapper import ReportNameMapper
from core.generator_planner import GeneratorPlanner


arguments = Arguments()
arguments = arguments.getArgs()

financial = pd.read_csv(arguments.financial_file, sep=';', header=11)
mapper = ReportNameMapper()

# credits = financial[financial['Montant'] > 0]
# debits = financial[financial['Montant'] < 0]

# first_day  = pd.Timestamp(financial.head(1)['Date'].item())
# last_day =  pd.Timestamp(financial.tail(1)['Date'].item())

# def add_space(nb=1):
#     for x in range(nb):
#         print('\

try:
    os.mkdir(f'{os.getcwd()}/hello')
    os.mkdir(f'{os.getcwd()}/hello/graphs') 
except:
    print('folder /hello already exists')


generatorPlanner = GeneratorPlanner()
stubs = generatorPlanner.getStubs()

generatorLoader = GeneratorLoader()
generatorLoader.generateReport(financial, stubs)



# print(financial)


# print(f"Ce rapport couvre la période du {first_day:%d/%m/%Y} au {last_day:%d/%m/%Y}")
# add_space(2)

# print("Revenus")

# print(f"nb = {len(credits)}")
# print(f"total = {credits['Montant'].sum()}")

# add_space(2)

# print("Dépenses")

# spending = Spendings()

# spending.generate(financial)
