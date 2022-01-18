from openpyxl import load_workbook

infile = load_workbook("products.xlsx")
 
product_list=infile["Table 1"]

products_per_supplier = {}
total_value_per_suplier = {}
products_under_10_inv = {}

for product_row in range(2, product_list.max_row + 1):
  supplier_name=product_list.cell(product_row, 4).value
  inventory = product_list.cell(product_row, 2).value
  price = product_list.cell(product_row, 3).value
  product_name = product_list.cell(product_row, 1).value
  inventory_price = product_list.cell(product_row, 5)
  
  #calculation number of products per supplier
  if supplier_name in products_per_supplier:
    current_num_products = products_per_supplier.get(supplier_name)
    products_per_supplier[supplier_name] = current_num_products + 1
  else:
    products_per_supplier[supplier_name] = 1  
    
  #calcualtion number of products per supplier
  if supplier_name in total_value_per_suplier:
      current_total_value = total_value_per_suplier.get(supplier_name)
      total_value_per_suplier[supplier_name] = current_total_value + inventory * price 
      
  else:
    total_value_per_suplier[supplier_name] = inventory * price
    
    
  #logic with inventory less than 10
  if inventory < 10:
    products_under_10_inv[int(product_name)]= int(inventory)
    
  #add inventory price
  inventory_price.value = inventory * price
infile.save('inventory_with_total_values.xlsx')

print(products_per_supplier)    
print(total_value_per_suplier)
print(products_under_10_inv)
