from keystoneauth1 import session
from keystoneauth1.identity.v3 import Token
from keystoneauth1.extras._saml2.v3.saml2 import Password as SAMLPassword
from keystoneclient.v3.client import Client

def get_federated_session(body):
    # authenticate to the idp
    saml_auth = SAMLPassword(auth_url=body["OS_AUTH_URL".lower()],
                             identity_provider=body["OS_IDENTITY_PROVIDER".lower()],
                             identity_provider_url=body["OS_IDENTITY_PROVIDER_URL".lower()],
                             username=body["OS_USERNAME".lower()],
                             password=body["OS_PASSWORD".lower()],
                             protocol=body["OS_PROTOCOL".lower()])

    # get first available project and scoped auth
    sess = session.Session(verify=False)
    unscoped_access_info = saml_auth.get_access(sess,verify=False)
    # unscoped_client = Client(session=sess, auth=saml_auth)
    #
    # # Get project with the given name
    # target_project = None
    # projects = unscoped_client.federation.projects.list()
    # for project in projects:
    #     if project.id == body["OS_PROJECT_ID".lower()]:
    #         target_project = project
    #
    # if not target_project:
    #     raise SystemExit("Project %s was not found" % body["OS_PROJECT_ID".lower()])

    # Create a session with a scoped token for the project
    unscoped_token = unscoped_access_info.auth_token
    scoped_token = Token(auth_url=saml_auth.auth_url,
                         token=unscoped_token,
                         project_id=body["OS_PROJECT_ID".lower()],
                         reauthenticate=False)
    token = scoped_token.get_token(sess)
    return token
    # federated_session = session.Session(auth=scoped_token,verify=False)
    # return target_project, federated_session


