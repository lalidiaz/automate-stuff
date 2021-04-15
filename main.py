import openpyxl

# Read our spreadsheet file.
inv_file = openpyxl.load_workbook("inventory.xlsx")

# Get the specific sheet I will work on.
product_list = inv_file["Sheet1"]

# Calculate how many products I have per supplier and list the name of
# the suppliers with that respective number of products.
prod_per_supplier = {}

print(product_list.max_row)
# Read how many products are in the list to iterate.
# start from 2 and end in the last row (including)
for product_row in range(2, product_list.max_row + 1):
   supplier_name = product_list.cell(product_row, 4).value

   if supplier_name in prod_per_supplier:
      current_num_products = prod_per_supplier.get(supplier_name)
      prod_per_supplier[supplier_name] = current_num_products + 1
   else:
      print("Adding a new supplier")
      prod_per_supplier[supplier_name] = 1

print(prod_per_supplier)

# Calculate the total inventory value per supplier:



