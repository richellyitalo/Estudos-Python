ips = open('ips.txt')
validos = open('ips_validos.txt', 'w')
invalidos = open('ips_invalidos.txt', 'w')

def ip_ok(ip):
    for ip in ip.split('.'):
        if int(ip) > 255:
            return False
    return True

for linha in ips.readlines():
    if ip_ok(linha):
        validos.write(linha)
    else:
        invalidos.write(linha)
ips.close()
validos.close()
invalidos.close()
    
