
# Programa para calcular o consumo de água com base no tipo de imóvel e no consumo em metros cúbicos (m³).

tipo_imovel= input ("Digite o tipo de imóvel (comercial,casa, apartamento): ")
consumo_agua= float(input("Digite o consumo de água em metros cúbicos(m³): ")) 
if tipo_imovel == "comercial":
        print("Tarifa comercial aplicada – consulte o plano corporativo.")
elif tipo_imovel == "apartamento" and consumo_agua < 10:
        print("Consumo econômico – excelente controle de água!")

elif tipo_imovel in ("apartamento", "casa") and consumo_agua <= 25:
        print("Consumo moderado – dentro do padrão residencial.")
else:
        print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
