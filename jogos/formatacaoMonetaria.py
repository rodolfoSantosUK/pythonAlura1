# sIGNIFICA que terao sete caracteres e receberá um float com 2 casas decimais
print(" R$ {:7.2f}".format(1.5))
print(" R$ {:7.2f}".format(4.5))
print(" R$ {:7.2f}".format(1234.5))

#Ao formatar data temos dois digitos preenchidos com 0 caso seja passado
# somente um valor como parametro
print("Data {:2d}/{:02d}".format(6,4))
print("Data {:02d}/{:02d}/{:4d}".format(19,11,2020))