# #gabarito 138

# nome_cidade = "Niterói"

# cordenadas = (latitude, longitude)

# results = cliente.places_nearby(location = cordenadas, 
#                                   keyword = f"Mc Donalds {nome_cidade}", radius = 10000)

# lista_dfs = []

# while True:
        
#         time.sleep(3)

#         for mc in results['results']:

#                     df = pd.DataFrame({'nome': mc['name'],
#                                   'endereco': mc['vicinity'],
#                                   'latitude': mc['geometry']['location']['lat'],
#                                   'longitudade': mc['geometry']['location']['lng']}, index = [0])

#                     lista_dfs.append(df)


#         if 'next_page_token' in results:
#             next_page_token = results['next_page_token']
#             results = cliente.places_nearby(location = cordenadas, 
#                                   keyword = f"Mc Donalds {nome_cidade}", radius = 50000, page_token = next_page_token)

#         else:
#             break
            

# lojas_mc = pd.concat(lista_dfs, ignore_index = True)
# lojas_mc