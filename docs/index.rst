Welcome to the juntagrico documentation
=======================================
Installation
------------

Install juntagrico from it's git repository or using pip. You need an django app.

The following django settings are nescessary to run juntagrico.

Additional to juntagrico the following apps have to installed into django:

.. code-block:: python

    INSTALLED_APPS = [
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.admin',
        'juntagrico',
        'impersonate',
    ]
    
The following authentication settings are required

.. code-block:: python

    AUTHENTICATION_BACKENDS = (
        'juntagrico.util.auth.AuthenticateWithEmail',
        'django.contrib.auth.backends.ModelBackend'
    )
    
Additionally also some changes in the middleware have to to be added

.. code-block:: python

    MIDDLEWARE = [
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'impersonate.middleware.ImpersonateMiddleware',
    ]
    
Since we use session we need a serializer

.. code-block:: python

    SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
    
Django also needs to be configured to send emails and to access a database. If you need more helping points see the testsettings in the project folder



juntagrico specific settings
----------------------------

You can use the following settings to configure juntagrico


* MEMBER_STRING

  The description text for memebers, if you use something special
  
  Type: String

  default value

  .. code-block:: python

    "Mitglied"

* MEMBERS_STRING

  Plural of the above

  Type: String

  default value
    
  .. code-block:: python

    "Mitglieder"

* ASSIGNMENT_STRING

  The description text for job assignemnts, if you use something special

  Type: String

  default value

  .. code-block:: python

    "Arbeitseinsatz" 

* ASSIGNMENTS_STRING

  Plural of the above

  Type: String

  default value

  .. code-block:: python

    "Arbeitseinsätze"

* ORGANISATION_NAME

  The short name of your orgnisation

  Type: String

  default value

  .. code-block:: python

    "Juntagrico"

* ORGANISATION_LONG_NAME

  The long version of your organisation, if you have one otherwise also use the short one
  
  Type: String

  default value

  .. code-block:: python

    "Juntagrico the best thing in the world"

* ORGANISATION_ADDRESS

  The address of your organisation
  
  Type: dict with the keys
  - name
  - street
  - number
  - zip
  - city
  - extra

  default value

  .. code-block:: python

    {"name":"Juntagrico", 
        "street" : "Fakestreet",
        "number" : "123",
        "zip" : "12456",
        "city" : "Springfield",
        "extra" : ""}

* ORGANISATION_PHONE

  The phone number for your organisation

  Type: string

  default value

  .. code-block:: python

    ""

* ORGANISATION_BANK_CONNECTION

  the bank connection informartion of your organisation
  
  Type: dict with the keys
  - PC (postkonto)
  - BIC
  - IBAN
  - NAME
  - ESR (if you enable billing)

  default value

  .. code-block:: python

    {"PC" : "01-123-5",
        "IBAN" : "CH 00 12345 67890 12345 67890 10",
        "BIC" : "BIC12345XX",
        "NAME" : "Juntagrico Bank",
        "ESR" : "01-123-45"}

* INFO_EMAIL

  The general administrative email of your organisation
  
  Type: String

  default value

  .. code-block:: python

    "info@juntagrico.juntagrico"

* GARDEN_EMAIL

  The email of the garden organisation team of your organisation.
  If not set, the INFO_EMAIL will be used by default.

  Type: String

  default value

  .. code-block:: python

    "INFO_EMAIL"

* SERVER_URL

  The base url of your organisation (not the one where you run juntagrico)

  Type: String  

  default value

  .. code-block:: python

    "www.juntagrico.juntagrico"

* ADMINPORTAL_NAME

  The name you want to use for the portal
  
  Type: String

  default value

  .. code-block:: python

    "my.juntagrico"

* ADMINPORTAL_SERVER_URL

  The base URL where you run juntagrico (and where your static lies)
  
  Type: String

  default value

  .. code-block:: python

    "my.juntagrico.juntagrico"

* BUSINESS_REGULATIONS

  URL to your business regulations document
  
  Type: String

  default value

  .. code-block:: python

    ""

* BYLAWS

  URL to your bylaws document
  
  Type: String

  default value

  .. code-block:: python

    ""

* MAIL_TEMPLATE

  Path to your custom html email template if you want to overwrite the look and feel of the html emails
  
  Type: String

  default value

  .. code-block:: python

    "mails/email.html"

* STYLE_SHEET

  If you want to use a custom design this specifies the path for your css
  
  Type: String

  default value

  .. code-block:: python

    "/static/css/personal.css"

* FAVICON

  If you want to use a custom favicon this specifies the path for your favicon
  
  Type: String

  default value

  .. code-block:: python

    "/static/img/favicon.ico"

* FAQ_DOC

  URL to your FAQ document
  
  Type: String

  default value

  .. code-block:: python

    ""

* BOOTSTRAP

  If you want to use a customized version of bootstrap this specifies the corresponding path for it
  
  Type: String

  default value

  .. code-block:: python

    "/static/external/bootstrap-3.3.1/css/bootstrap.min.css"

* EXTRA_SUB_INFO

  If you use extra subscriptions this describes the URL to the document describing them
  
  Type: String

  default value

  .. code-block:: python

    ""

* ACTIVITY_AREA_INFO

  URL to your document describing your activity areas
  
  Type: String

  default value

  .. code-block:: python

    ""

* SHARE_PRICE

  Price of one share
  
  Type: String

  default value
  
  .. code-block:: python

    "250"

* BASE_FEE

  Yearly fee for members without a subscription
  
  Type: String

  default value
  
  .. code-block:: python

    ""

* CURRENCY

  The default currency used within the system
  
  Type: String

  default value
  
  .. code-block:: python

    "CHF"

* ASSIGNMENT_UNIT

  The mode how assignments are counted: Valid values are EMTITY and HOURS. ENTITY the assignments are counted by occurrence, Hours the value of the assignments are counted by the actual time the user spent on a job.
  
  Type: String

  default value
  
  .. code-block:: python

    "ENTITY"

* PROMOTED_JOB_TYPES

  Types of jobs which should apear on start page
  
  Type: List of Strings

  default value

  .. code-block:: python

    []

* PROMOTED_JOBS_AMOUNT

  Amount of jobs which should be promoted on the startpage
  
  Type: Integer

  default value

  .. code-block:: python

    2

* DEPOT_LIST_GENERATION_DAYS

  Days on which the deliverylist can be generated
  
  Type: List of Integers representing days of the week

  default value

  .. code-block:: python

    [1,2,3,4,5,6,7]

* BILLING

  Enabling bill generation and management
  
  Type: Boolean

  default value

  .. code-block:: python

    False

* BUSINESS_YEAR_START

  Defining the start of the business year
  
  Type: dict with the keys
  - day
  - month

  default value

  .. code-block:: python

    {"day":1, "month":1}

* BUSINESS_YEAR_CANCELATION_MONTH

  The date until you can cancel your subscriptions
  
  Type: Integer

  default value

  .. code-block:: python

    12

* MEMBERSHIP_END_MONTH

  The month at which end the members can leave the organisation
  
  Type: Integer

  default value

  .. code-block:: python

    6

* DEMO_USER

  If you run a demo setup and want to display the login name on the login page
  
  Type: String

  default value

  .. code-block:: python

    ''

* DEMO_PWD

  If you run a demo setup and want to display the password on the login page

  default value

  .. code-block:: python

    ''

* IMAGES

  Defining the different images for core and job assignments etc

  default value

  .. code-block:: python

    {'status_100': '/static/img/status_100.png', 
        'status_75': '/static/img/status_75.png', 
        'status_50': '/static/img/status_50.png', 
        'status_25': '/static/img/status_25.png', 
        'status_0': '/static/img/status_0.png', 
        'single_full': '/static/img/single_full.png', 
        'single_empty': '/static/img/single_empty.png', 
        'single_core': '/static/img/single_core.png',
        'core': '/static/img/core.png'}

* EMAILS

  Defining the different email templates

  default value

  .. code-block:: python

    {
        'welcome': 'mails/welcome_mail.txt',
        'co_welcome': 'mails/welcome_added_mail.txt',
        'co_added': 'mails/added_mail.txt',
        'password': 'mails/password_reset_mail.txt',
        'j_reminder': 'mails/job_reminder_mail.txt',
        'j_canceled': 'mails/job_canceled_mail.txt',
        'confirm': 'mails/confirm.txt',
        'j_changed': 'mails/job_time_changed_mail.txt',
        'j_signup': 'mails/job_signup_mail.txt',
        'd_changed': 'mails/depot_changed_mail.txt',
        's_created': 'mails/share_created_mail.txt',
        'n_sub': 'mails/new_subscription.txt',
        's_canceled': 'mails/subscription_canceled_mail.txt',
        'm_canceled': 'mails/membership_canceled_mail.txt',
        'b_share': 'mails/bill_share.txt',
        'b_sub': 'mails/bill_sub.txt',
        'b_esub': 'mails/bill_extrasub.txt'
    }

* GOOGLE_API_KEY

  The google api key to enable the mapps in juntagrico
  
  Type: String

  default value

  .. code-block:: python

    "GOOGLE_API_KEY"

For your convenience all settings with default values to copy into your settings.py and to adapt them

  .. code-block:: python

    MEMBER_STRING = 'Mitglied'
    MEMBERS_STRING = 'Mitglieder'
    ASSIGNMENT_STRING = 'Arbeitseinsatz'
    ASSIGNMENTS_STRING = 'Arbeitseinsätze'
    ORGANISATION_NAME = 'Juntagrico'
    ORGANISATION_LONG_NAME = 'Juntagrico the best thing in the world'
    ORGANISATION_ADDRESS = {'name':'Juntagrico',
                        'street' : 'Fakestreet',
                        'number' : '123',
                        'zip' : '12456',
                        'city' : 'Springfield',
                        'extra' : ''}
    ORGANISATION_BANK_CONNECTION = {'PC' : '01-123-5', 
                                'IBAN' : 'CH 00 12345 67890 12345 67890 10', 
                                'BIC' : 'BIC12345XX', 
                                'NAME' : 'Juntagrico Bank', 
                                'ESR' : '01-123-45'}
    INFO_EMAIL = 'info@juntagrico.juntagrico'
    GARDEN_EMAIL = 'garten@juntagrico.juntagrico'
    SERVER_URL = 'www.juntagrico.juntagrico'
    ADMINPORTAL_NAME = 'my.juntagrico'
    ADMINPORTAL_SERVER_URL = 'my.juntagrico.juntagrico'
    BUSINESS_REGULATIONS = '/static/docs/business_regulations.pdf'
    BYLAWS = '/static/docs/bylaws.pdf'
    MAIL_TEMPLATE = 'mails/email.html'
    STYLE_SHEET = '/static/css/personal.css'
    FAVICON = '/static/img/favicon.ico'
    BOOTSTRAP = '/static/external/bootstrap-3.3.1/css/bootstrap.min.css'
    FAQ_DOC = '/static/doc/fac.pdf'
    EXTRA_SUB_INFO = '/static/doc/extra_sub_info.pdf'
    ACTIVITY_AREA_INFO = '/static/doc/activity_area_info.pdf'
    SHARE_PRICE = '250'
    CURRENCY = 'CHF'
    ASSIGNMENT_UNIT = 'ENTITY'
    PROMOTED_JOB_TYPES = []
    PROMOTED_JOBS_AMOUNT = 2
    DEPOT_LIST_COVER_SHEETS = 'x'
    DEPOT_LIST_OVERVIEWS = 'x'
    DEPOT_LIST_GENERATION_DAYS = [1,2,3,4,5,6,7]	
    BILLING = False
    BUSINESS_YEAR_START = {'day':1, 'month':1}
    BUSINESS_YEAR_CANCELATION_MONTH = 12
    DEMO_USER = ''
    DEMO_PWD = ''
    IMAGES[key] = {'status_100': '/static/img/status_100.png', 
                'status_75': '/static/img/status_75.png', 
                'status_50': '/static/img/status_50.png', 
                'status_25': '/static/img/status_25.png', 
                'status_0': '/static/img/status_0.png', 
                'single_full': '/static/img/single_full.png', 
                'single_empty': '/static/img/single_empty.png', 
                'single_core': '/static/img/single_core.png',
                'core': '/static/img/core.png'}
    GOOGLE_API_KEY = 'GOOGLE_API_KEY'
    EMAILS = {
        'welcome': 'mails/welcome_mail.txt',
        'co_welcome': 'mails/welcome_added_mail.txt',
        'co_added': 'mails/added_mail.txt',
        'password': 'mails/password_reset_mail.txt',
        'j_reminder': 'mails/job_reminder_mail.txt',
        'j_canceled': 'mails/job_canceled_mail.txt',
        'confirm': 'mails/confirm.txt',
        'j_changed': 'mails/job_time_changed_mail.txt',
        'j_signup': 'mails/job_signup_mail.txt',
        'd_changed': 'mails/depot_changed_mail.txt',
        's_created': 'mails/share_created_mail.txt',
        'n_sub': 'mails/new_subscription.txt',
        's_canceled': 'mails/subscription_canceled_mail.txt',
        'm_canceled': 'mails/membership_canceled_mail.txt',
        'b_share': 'mails/bill_share.txt',
        'b_sub': 'mails/bill_sub.txt',
        'b_esub': 'mails/bill_extrasub.txt'
    }
    BASE_FEE = ''
    ORGANISATION_PHONE = ''
    
    
Release Notes
=============

1.1.3
-----
 No migrations

* Fixed Typo in Billable
* Empty strings as default for settings containing a url to a document
* Empty url configs prevent link from being displayed in templates
* fix for waiting list and paid shares
* empty strings in profile IBAN field form are not validated anymore
* doc updated
* error in onetime job fixed
