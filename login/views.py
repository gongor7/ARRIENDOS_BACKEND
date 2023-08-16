from django.shortcuts import render
from ldap3 import Server, Connection, ALL, SUBTREE, ALL_ATTRIBUTES
from ldap3.core.exceptions import LDAPException
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
def get_userldap(request):
    ldap_server = '172.16.1.31:3890'
    ldap_user = 'cn=admin,dc=muserpol,dc=gob,dc=bo'
    ldap_password = 't1lnrzi_2_VICqNntFlWs2UV'  
    server = Server(ldap_server, get_info=ALL)
    connection = Connection(server, ldap_user, ldap_password, auto_bind=True)
    search_base = 'dc=muserpol,dc=gob,dc=bo'
    usuario1 = "ahara"
    user_dn = f"uid={usuario1},ou=usuarios,dc=muserpol,dc=gob,dc=bo"
    password = "12345678"
    try:
        with Connection(server, user_dn, password, auto_bind=True):
            return JsonResponse({ "estado": "el usuario existe"}, status=202)
    except:
            return JsonResponse({ "estado": "el usuario no existe"}, status=404)