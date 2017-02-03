from django.shortcuts import render_to_response
from django.http import HttpResponse
from jira.client import JIRA
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import ldap
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.sessions.backends.db import SessionStore

# Create your views here.

import jwt
import logging
import urllib
import ssl
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.backends import default_backend
from django.conf import settings
from django.http import HttpResponseForbidden
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.views.generic import View
from django.http import HttpResponse

logger = logging.getLogger('main')


class SSOLoginView(View):
    """
    SSOlogin view redirects user to SSO Login URL, verifies the jwt token and
    log's in a user.
    """

    def get_public_key(self):
        # Convert from PEM to DER
        try:
            pem = ssl.get_server_certificate((settings.SSO_FQDN, 443), ssl_version=ssl.PROTOCOL_TLSv1)
        except Exception as e:
            logger.error('Error fetching certificate from %s' % settings.SSO_FQDN)
            return None

        certificate_text = pem
        certificate = load_pem_x509_certificate(certificate_text, default_backend())
        publickey = certificate.public_key()
        return publickey

    def verify_jwt(self, jwt_param):
        # PyCrypto does not directly support extracting a public key from an
        # X509 cert file. Need to use a low level primitive to extract it.
        # See: https://gist.github.com/piotrbulinski/ba553b21652ea1e9601a
        public_key = self.get_public_key()
        try:
            jwt_token = jwt.decode(jwt_param, public_key, algorithms=['RS256'],  verify_expiration=True, leeway=10, audience=settings.SERVICE_FQDN)
        except jwt.ExpiredSignature:
            logger.info('Expired signature on JWT'  )
            jwt_token = None
        except jwt.DecodeError:
            logger.info('Failed to verify signature on JWT')
            jwt_token = None
        except jwt.InvalidAudienceError:
            logger.info('Invalid Audience, please check your SERVICE_FQDN paramter')
            jwt_token = None
        return jwt_token

    def get(self, request):
        """
        Redirects user to ``SSO_ENDPOINT`` if unauthenticated, parses the JWT send by ``SSO_ENDPOINT``
        and redirects user to the ``orig_uri`` (requested page)
        :param request:
        :return str: HTTPRedirect
        """
        if request.user.is_authenticated():
            orig_uri = request.GET.get('orig_uri', settings.APPLICATION_LANDING_URL)
            return redirect(orig_uri)

        jwt_param = request.GET.get('jwt', None)

        if jwt_param:
            # Verify JWT
            jwt_token = self.verify_jwt(jwt_param)
            if not jwt_token:
                return HttpResponseForbidden('Unable to verify login, try clearing your cookies and log in <a href="/login/">again</a>. '
                                             'If problem persists, please contact the administrator.')
            else:
                username = jwt_token['u']
                auth_realm = jwt_token['realm']
                groups = jwt_token['g']
                timestamp = jwt_token['exp']
                aud = jwt_token['aud']
                orig_uri = jwt_token['orig_uri']
                jti = jwt_token['jti']
                state = jwt_token['state']
                email = jwt_token['email']
                username = username.split('@')[0]
                logger.info(
                    'Verified: user=%s email:%s groups=%s auth_realm=%s expiry=%s' % (username, email, groups, auth_realm, timestamp))
                auth_session = username

                # Call authenticate method to set the backend and create
                # user if it does not exist
                user = authenticate(username=username, email=email)
                if user is None:
                    return HttpResponseForbidden('Error authenticating %s' % username)
                else:
                    # Set the login and session cookies
                    login(request, user)

                logger.info('Redirecting to: %s' % orig_uri)
                return redirect(orig_uri)

        orig_uri = request.GET.get('orig_uri', None)
        if orig_uri is None:
            orig_uri = request.GET.get('next', settings.APPLICATION_LANDING_URL)
        verification_uri = settings.SSO_VERIFICATION_URL

        login_redirect = '%s?%s' % (
            settings.SSO_ENDPOINT,
            urllib.urlencode(
                [('redirect_uri', verification_uri),
                 ('orig_uri', orig_uri),
                 ('logout', '/logout')]))

            # Redirect to the SSO server for user authentication
        return redirect(login_redirect)




def index(request):
    return render_to_response('search.html')

def results(request):
        if 'name' in request.GET:
                n=request.GET['name']
		request.session['n']=n
		ldapobject = ldap.ldapobject.SimpleLDAPObject(uri=settings.AD_LDAP_URL)
                ldapobject.start_tls_s()
                ldapobject.protocol_version = ldap.VERSION3
                ldapobject.ldap_page_size = 10000
                ldapobject.set_option(ldap.OPT_REFERRALS, 0)
                ldapobject.bind_s(settings.AD_SEARCH_DN,settings.AD_PASSWORD,ldap.AUTH_SIMPLE)
                serch_result = ldapobject.search_ext_s('ou=inmobians,dc=corp,dc=inmobi,dc=com',ldap.SCOPE_SUBTREE,'(sAMAccountName=%s)'%(n),['manager','name','EmployeeNumber','mobile','mail','department'])
                txt = serch_result[0]
                dxt = list(txt)
                df = dxt[1:]
		mng = df[0]['manager']
		mag = ''.join(mng).split(',')[0].split('=')[1]
                if 'mobile' in df[0]:
                        l=[df[0]['name'],df[0]['mobile'],df[0]['employeeNumber'],df[0]['mail'],df[0]['department']]
                        items=[val for sublist in l for val in sublist]
                        bg = {'Name':items[0],'Email':items[3],'Contact':items[1],'Dept':items[4],'Manager':mag,'ID':items[2]}
			request.session['bg']=bg
#                       return HttpResponse(df)
                        return render_to_response('results.html', {'bg':bg})
                else:
                        l=[df[0]['name'],df[0]['employeeNumber'],df[0]['mail'],df[0]['department']]
                        items=[val for sublist in l for val in sublist]
                        bg = {'Name':items[0],'Email':items[2],'Contact':'','Dept':items[3],'Manager':mag,'ID':items[1]}
			request.session['bg']=bg
                        return render_to_response('results.html', {'bg':bg})

	else:
		return HttpResponse('Please enter a valid input.')


#dict={'None':"-1",'VM':"12607",'Desktop':"12608","Laptop":"12609","Mobile":"12610","Network":"12611","Server":"12612","Other":"12613","Printer":"13206","Account lockouts/Passwd":"13613","Google Apps":"13614","Access Requests":"13615","Wireless":"13616","Conference Room":"13617","Virus Malware":"13618","Vpn":"13619"}


def create(request):
#	global dict
	bg = request.session['bg']
	n = request.session['n']
	if 'desc'and 'summary'  and 'customfield_14635' in request.GET:
		d=request.GET['desc']
		s=request.GET['summary']
		t=request.GET['customfield_14635']
		options={'server':'http://jira.corp.inmobi.com'}
		jira=JIRA(options,basic_auth=('jira.walkup',IDP_JIRA_PASSWORD))
                root_dict={
                'project':{'key':'TS'},
		'issuetype':{'name':'Issue'},
                'summary':s,
		'description':d,
		'customfield_15712':[{'id':'13608'}],
		'customfield_15201':{'name':n},
		'customfield_14635':{'id':t},
	         }
		my_issue=jira.create_issue(fields=root_dict)

	return render_to_response('test.html',{'bg':bg})
