import pandas as pd
import os

# TODO :https://www.cms.gov/medicare/medicare-part-b-drug-average-sales-price/2021-asp-drug-pricing-files, for part B
# TODO: find Part D, NADAC
# TODO: find these files, scrap them off the internet, link/union/analyze them
# TODO: create seperate branch, pull request, then merge
# TODO: convert intermediate files to parquet, index=False


'''
Problem statement: dynamically pull and link these files, build Jupyter notebook, publish to github

# partd_pricing_2020Q4
  filepath: "${raw_folder}/price/pricing_file_PPUF_2020Q4.parquet"

# partd_pricing_2020Q3
  filepath: "${raw_folder}/price/pricing_file_PPUF_2020Q3.parquet"

# partd_pricing_2020Q2
  filepath: "${raw_folder}/price/pricing_file_PPUF_2020Q2.parquet"
    
# partd_pricing_2020Q1
  filepath: "${raw_folder}/price/pricing_file_PPUF_2020Q1.parquet"
    
# partd_pricing_2019Q4
  filepath: "${raw_folder}/price/pricing_file_PPUF_2019Q4.parquet"
    
# partd_pricing_2019Q3
  filepath: "${raw_folder}/price/pricing_file_PPUF_2019Q3.parquet"

# partd_pricing_2019Q2
  filepath: "${raw_folder}/price/pricing_file_PPUF_2019Q2.parquet"

# partd_pricing_2019Q1
  filepath: "${raw_folder}/price/pricing_file_PPUF_2019Q1.parquet"
    
# NADAC pricing data
"${raw_folder}/price/NADAC__National_Average_Drug_Acquisition_Cost_20210311.csv"
    
# Part B pricing data
  filepath: "${raw_folder}/price/April_2021_asp_pricing.csv"
  encoding: "windows-1254"
    
# Part B pricing crosswalk
  filepath: "${raw_folder}/price/April_2021_asp_crosswalk.csv"
    inferSchema: True
    encoding: "windows-1254"
'''