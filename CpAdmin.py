#!/usr/bin/env python3
#Programmer:Ayman Mahmoud Alaiwah

import urllib.request
from optparse import *



############[ Start Function ]##############
def logo():
	print("""
	 _______  _______    _______  ______   _______ _________ _       
	(  ____ \(  ____ )  (  ___  )(  __  \ (       )\__   __/( (    /|
	| (    \/| (    )|  | (   ) || (  \  )| () () |   ) (   |  \  ( |
	| |      | (____)|  | (___) || |   ) || || || |   | |   |   \ | |
	| |      |  _____)  |  ___  || |   | || |(_)| |   | |   | (\ \) |
	| |      | (        | (   ) || |   ) || |   | |   | |   | | \   |
	| (____/\| )        | )   ( || (__/  )| )   ( |___) (___| )  \  |
	(_______/|/         |/     \|(______/ |/     \|\_______/|/    )_)

	-----------------------------[InFo]------------------------------

	Programmer          : Ayman Mahmoud Alaiwah
	PageFacebook        : https://www.facebook.com/progaymanalaiwah
	Number Cpanel Admin : 1086                                                               
	""")
logo()
#OPtion Parser
parser = OptionParser("""

CpAdmin.py [Options]
--------------------
-u      Url WebSite Search Cpanel Admin
-e      Shwo Error Url Not Found  run -e 1
-S      Save Url Not Found -S Name File
-s      Save Url Found  -s name file

 
	""") 
parser.add_option("-u","--url",dest="url",type="string",help="CpAdmin.py -u Url")
parser.add_option("-e","--error",dest="error",type="string",help="CpAdmin.py -u http://www.example.com/ -e 1")
parser.add_option("-s","--save",dest="save",type="string",help="CpAdmin.py -u http://www.example.com/ -s NameFile")
parser.add_option("-S","--esave",dest="esave",type="string",help="CpAdmin.py -u http://www.example.com/ -S NameFile")
(options,args) = parser.parse_args()

if options.url != None:
	url = options.url
	error = options.error
	save = options.save
	esave = options.esave
	if save != None:
	  saveurl = open(save,"w")
	  saveurl.write("")
	if esave != None:
	  saveurl = open(esave,"w")
	  saveurl.write("")
	try:
		CpAdminList = ['login.htm', 'login.html', 'login/', 'login.%EXT%', 'adm/', 'admin/', 'admin/account.html', 'admin/login.html', 
		 'admin/login.htm', 'admin/home.%EXT%', 'admin/controlpanel.html', 'admin/controlpanel.htm', 'admin/cp.%EXT%', 
		 'admin/adminLogin.html', 'admin/adminLogin.htm', 'admin/admin_login.%EXT%', 'admin/controlpanel.%EXT%', 
		 'admin/admin-login.%EXT%', 'admin-login.%EXT%', 'admin/account.%EXT%', 'admin/admin.%EXT%', 'admin.htm', 'admin.html', 
		 'adminitem/', 'adminitem.%EXT%', 'adminitems/', 'adminitems.%EXT%', 'administrator/', 'administrator/login.%EXT%', 
		 'administrator.%EXT%', 'administration/', 'administration.%EXT%', 'adminLogin/', 'adminlogin.%EXT%', 'admin_area/admin.%EXT%',
		  'admin_area/', 'admin_area/login.%EXT%', 'manager/', 'manager.%EXT%', 'letmein/', 'letmein.%EXT%', 'superuser/',
		   'superuser.%EXT%', 'access/', 'access.%EXT%', 'sysadm/', 'sysadm.%EXT%', 'superman/', 'supervisor/', 'panel.%EXT%', 
		   'control/', 'control.%EXT%', 'member/', 'member.%EXT%', 'members/', 'members.%EXT%', 'user/', 'user.%EXT%', 'cp/', 
		   'uvpanel/', 'manage/', 'manage.%EXT%', 'management/', 'management.%EXT%', 'signin/', 'signin.%EXT%', 'log-in/', 
		   'log-in.%EXT%', 'log_in/', 'log_in.%EXT%', 'sign_in/', 'sign_in.%EXT%', 'sign-in/', 'sign-in.%EXT%', 'users/', 
		   'users.%EXT%', 'accounts/', 'accounts.%EXT%', 'wp-login.php', 'bb-admin/login.%EXT%', 'bb-admin/admin.%EXT%', 
		   'bb-admin/admin.html', 'administrator/account.%EXT%', 'relogin.htm', 'relogin.html', 'check.%EXT%', 'relogin.%EXT%', 
		   'blog/wp-login.%EXT%', 'user/admin.%EXT%', 'users/admin.%EXT%', 'registration/', 'processlogin.%EXT%', 'checklogin.%EXT%', 
		   'checkuser.%EXT%', 'checkadmin.%EXT%', 'isadmin.%EXT%', 'authenticate.%EXT%', 'authentication.%EXT%', 'auth.%EXT%', 
		   'authuser.%EXT%', 'authadmin.%EXT%', 'cp.%EXT%', 'modelsearch/login.%EXT%', 'moderator.%EXT%', 'moderator/', 'controlpanel/', 
		   'controlpanel.%EXT%', 'admincontrol.%EXT%', 'adminpanel.%EXT%', 'fileadmin/', 'fileadmin.%EXT%', 'sysadmin.%EXT%', 
		   'admin1.%EXT%', 'admin1.html', 'admin1.htm', 'admin2.%EXT%', 'admin2.html', 'yonetim.%EXT%', 'yonetim.html', 'yonetici.%EXT%', 
		   'yonetici.html', 'phpmyadmin/', 'myadmin/', 'ur-admin.%EXT%', 'ur-admin/', 'Server.%EXT%', 'Server/', 'wp-admin/', 
		   'administr8.%EXT%', 'administr8/', 'webadmin/', 'webadmin.%EXT%', 'administratie/', 'admins/', 'admins.%EXT%', 'administrivia/', 
		   'Database_Administration/', 'useradmin/', 'sysadmins/', 'admin1/', 'system-administration/', 'administrators/', 'pgadmin/', 
		   'directadmin/', 'staradmin/', 'ServerAdministrator/', 'SysAdmin/', 'administer/', 'LiveUser_Admin/', 'sys-admin/', 'typo3/', 
		   'panel/', 'cpanel/', 'cpanel_file/', 'platz_login/', 'rcLogin/', 'blogindex/', 'formslogin/', 'autologin/', 'support_login/', 
		   '****_login/', 'manuallogin/', 'simpleLogin/', 'loginflat/', 'utility_login/', 'showlogin/', 'memlogin/', 'login-redirect/', 
		   'sub-login/', 'wp-login/', 'login1/', 'dir-login/', 'login_db/', 'xlogin/', 'smblogin/', 'customer_login/', 'UserLogin/', 
		   'login-us/', 'acct_login/', 'bigadmin/', 'project-admins/', 'phppgadmin/', 'pureadmin/', 'sql-admin/', 'radmind/', 'openvpnadmin/', 
		   'wizmysqladmin/', 'vadmind/', 'ezsqliteadmin/', 'hpwebjetadmin/', 'newsadmin/', 'adminpro/', 'Lotus_Domino_Admin/', 'bbadmin/', 
		   'vmailadmin/', 'Indy_admin/', 'ccp14admin/', 'irc-macadmin/', 'banneradmin/', 'sshadmin/', 'phpldapadmin/', 'macadmin/', 
		   'administratoraccounts/', 'admin4_account/', 'admin4_colon/', 'radmind-1/', 'Super-Admin/', 'AdminTools/', 'cmsadmin/', 'SysAdmin2/', 
		   'globes_admin/', 'cadmins/', 'phpSQLiteAdmin/', 'navSiteAdmin/', 'server_admin_small/', 'logo_sysadmin/', 'power_user/', 
		   'system_administration/', 'ss_vms_admin_sm/', 'bb-admin/', 'panel-administracion/', 'instadmin/', 'memberadmin/', 'administratorlogin/',
		    'adm.%EXT%', 'admin_login.%EXT%', 'panel-administracion/login.%EXT%', 'pages/admin/admin-login.%EXT%', 'pages/admin/', 'acceso.%EXT%', 
		    'admincp/login.%EXT%', 'admincp/', 'adminarea/', 'admincontrol/', 'affiliate.%EXT%', 'adm_auth.%EXT%', 'memberadmin.%EXT%', 
		    'administratorlogin.%EXT%', 'modules/admin/', 'administrators.%EXT%', 'siteadmin/', 'siteadmin.%EXT%', 'adminsite/', 'kpanel/', 
		    'vorod/', 'vorod.%EXT%', 'vorud/', 'vorud.%EXT%', 'adminpanel/', 'PSUser/', 'secure/', 'webmaster/', 'webmaster.%EXT%', 
		    'autologin.%EXT%', 'userlogin.%EXT%', 'admin_area.%EXT%', 'cmsadmin.%EXT%', 'security/', 'usr/', 'root/', 'secret/', 
		    'admin/login.%EXT%', 'admin/adminLogin.%EXT%', 'moderator.php', 'moderator.html', 'moderator/login.%EXT%', 'moderator/admin.%EXT%', 
		    'yonetici.%EXT%', '0admin/', '0manager/', 'aadmin/', 'cgi-bin/login%EXT%', 'login1%EXT%', 'login_admin/', 'login_admin%EXT%', 
		    'login_out/', 'login_out%EXT%', 'login_user%EXT%', 'loginerror/', 'loginok/', 'loginsave/', 'loginsuper/', 'loginsuper%EXT%', 
		    'login%EXT%', 'logout/', 'logout%EXT%', 'secrets/', 'super1/', 'super1%EXT%', 'super_index%EXT%', 'super_login%EXT%', 
		    'supermanager%EXT%', 'superman%EXT%', 'superuser%EXT%', 'supervise/', 'supervise/Login%EXT%', 'super%EXT%', 'admin', 'adm', 
		    'admincp', 'admcp', 'cp', 'modcp', 'moderatorcp', 'adminare', 'admins', 'cpanel', 'controlpanel', 'admin1.php', 'admin1.html', 
		    'admin2.php', 'admin2.html', 'yonetim.php', 'yonetim.html', 'yonetici.php', 'yonetici.html', 'ccms/', 'ccms/login.php', 
		    'ccms/index.php', 'maintenance/', 'webmaster/', 'adm/', 'configuration/', 'configure/', 'websvn/', 'admin/', 'admin/account.php', 
		    'admin/account.html', 'admin/index.php', 'admin/index.html', 'admin/login.php', 'admin/login.html', 'admin/home.php', 
		    'admin/controlpanel.html', 'admin/controlpanel.php', 'admin.php', 'admin.html', 'admin/cp.php', 'admin/cp.html', 'cp.php', 
		    'cp.html', 'administrator/', 'administrator/index.html', 'administrator/index.php', 'administrator/login.html', 
		    'administrator/login.php', 'administrator/account.html', 'administrator/account.php', 'administrator.php', 'administrator.html', 
		    'login.php', 'login.html', 'modelsearch/login.php', 'moderator.php', 'moderator.html', 'moderator/login.php', 'moderator/login.html', 
		    'moderator/admin.php', 'moderator/admin.html', 'moderator/', 'account.php', 'account.html', 'controlpanel/', 'controlpanel.php', 
		    'controlpanel.html', 'admincontrol.php', 'admincontrol.html', 'adminpanel.php', 'adminpanel.html', 'admin1.asp', 'admin2.asp', 
		    'yonetim.asp', 'yonetici.asp', 'admin/account.asp', 'admin/index.asp', 'admin/login.asp', 'admin/home.asp', 'admin/controlpanel.asp', 
		    'admin.asp', 'admin/cp.asp', 'cp.asp', 'administrator/index.asp', 'administrator/login.asp', 'administrator/account.asp', 
		    'administrator.asp', 'login.asp', 'modelsearch/login.asp', 'moderator.asp', 'moderator/login.asp', 'moderator/admin.asp', 
		    'account.asp', 'controlpanel.asp', 'admincontrol.asp', 'adminpanel.asp', 'fileadmin/', 'fileadmin.php', 'fileadmin.asp', 
		    'fileadmin.html', 'administration/', 'administration.php', 'administration.html', 'sysadmin.php', 'sysadmin.html', 'phpmyadmin/', 
		    'myadmin/', 'sysadmin.asp', 'sysadmin/', 'ur-admin.asp', 'ur-admin.php', 'ur-admin.html', 
		    'ur-admin/ Server.php Server.html Server.asp Server/', 'wp-admin/', 'administr8.php', 'administr8.html', 'administr8/', 
		    'administr8.asp', 'webadmin/', 'webadmin.php', 'webadmin.asp', 'webadmin.html', 'administratie/', 'admins/', 'admins.php', 
		    'admins.asp', 'admins.html', 'administrivia/ Database_Administration/ WebAdmin/', 'useradmin/', 'sysadmins/', 'admin1/', 
		    'system-administration/', 'administrators/', 'pgadmin/', 'directadmin/', 'staradmin/ ServerAdministrator/ SysAdmin/', 
		    'administer/ LiveUser_Admin/', 'sys-admin/', 'typo3/', 'panel/', 'cpanel/', 'cPanel/', 'cpanel_file/', 'platz_login/', 'rcLogin/', 
		    'blogindex/', 'formslogin/', 'autologin/', 'support_login/', '****_login/', 'manuallogin/', 'simpleLogin/', 'loginflat/', 
		    'utility_login/', 'showlogin/', 'memlogin/', 'members/', 'login-redirect/ sub-login/', 'wp-login/', 'login1/', 'dir-login/', 
		    'login_db/', 'xlogin/', 'smblogin/', 'customer_login/ UserLogin/', 'login-us/', 'acct_login/', 'admin_area/', 'bigadmin/', 
		    'project-admins/', 'phppgadmin/', 'pureadmin/', 'sql-admin/', 'radmind/', 'openvpnadmin/', 'wizmysqladmin/', 'vadmind/', 
		    'ezsqliteadmin/', 'hpwebjetadmin/', 'newsadmin/', 'adminpro/ Lotus_Domino_Admin/', 'bbadmin/', 'vmailadmin/ Indy_admin/', 
		    'ccp14admin/', 'irc-macadmin/', 'banneradmin/', 'sshadmin/', 'phpldapadmin/', 'macadmin/', 'administratoraccounts/', 'admin4_account/', 
		    'admin4_colon/', 'radmind-1/ Super-Admin/ AdminTools/', 'cmsadmin/ SysAdmin2/', 'globes_admin/', 'cadmins/', 'phpSQLiteAdmin/', 
		    'navSiteAdmin/', 'server_admin_small/', 'logo_sysadmin/', 'server/', 'database_administration/', 'power_user/', 'system_administration/',
		     'ss_vms_admin_sm/', 'adminarea/', 'bb-admin/', 'adminLogin/', 'panel-administracion/', 'instadmin/', 'memberadmin/', 
		     'administratorlogin/', 'admin/admin.php', 'admin_area/admin.php', 'admin_area/login.php', 'siteadmin/login.php', 
		     'siteadmin/index.php', 'siteadmin/login.html', 'admin/admin.html', 'admin_area/index.php', 'bb-admin/index.php', 
		     'bb-admin/login.php', 'bb-admin/admin.php', 'admin_area/login.html', 'admin_area/index.html', 'admincp/index.asp',
		      'admincp/login.asp', 'admincp/index.html', 'webadmin/index.html', 'webadmin/admin.html', 'webadmin/login.html', 
		      'admin/admin_login.html', 'admin_login.html', 'panel-administracion/login.html', 'nsw/admin/login.php', 'webadmin/login.php', 
		      'admin/admin_login.php', 'admin_login.php', 'admin_area/admin.html', 'pages/admin/admin-login.php', 'admin/admin-login.php', 
		      'admin-login.php', 'bb-admin/index.html', 'bb-admin/login.html', 'bb-admin/admin.html', 'admin/home.html', 
		      'pages/admin/admin-login.html', 'admin/admin-login.html', 'admin-login.html', 'admin/adminLogin.html', 'adminLogin.html',
		       'home.html', 'rcjakar/admin/login.php', 'adminarea/index.html', 'adminarea/admin.html', 'webadmin/index.php', 'webadmin/admin.php', 
		       'user.html', 'modelsearch/login.html', 'adminarea/login.html', 'panel-administracion/index.html', 'panel-administracion/admin.html',
		        'modelsearch/index.html', 'modelsearch/admin.html', 'admincontrol/login.html', 'adm/index.html', 'adm.html', 'user.php', 
		        'panel-administracion/login.php', 'wp-login.php', 'adminLogin.php', 'admin/adminLogin.php', 'home.php', 'adminarea/index.php', 
		        'adminarea/admin.php', 'adminarea/login.php', 'panel-administracion/index.php', 'panel-administracion/admin.php', 
		        'modelsearch/index.php', 'modelsearch/admin.php', 'admincontrol/login.php', 'adm/admloginuser.php', 'admloginuser.php', 
		        'admin2/login.php', 'admin2/index.php', 'adm/index.php', 'adm.php', 'affiliate.php', 'adm_auth.php', 'memberadmin.php', 
		        'administratorlogin.php', 'admin/admin.asp', 'admin_area/admin.asp', 'admin_area/login.asp', 'admin_area/index.asp', 
		        'bb-admin/index.asp', 'bb-admin/login.asp', 'bb-admin/admin.asp', 'pages/admin/admin-login.asp', 'admin/admin-login.asp', 
		        'admin-login.asp', 'user.asp', 'webadmin/index.asp', 'webadmin/admin.asp', 'webadmin/login.asp', 'admin/admin_login.asp', 
		        'admin_login.asp', 'panel-administracion/login.asp', 'adminLogin.asp', 'admin/adminLogin.asp', 'home.asp', 'adminarea/index.asp', 
		        'adminarea/admin.asp', 'adminarea/login.asp', 'panel-administracion/index.asp', 'panel-administracion/admin.asp', 
		        'modelsearch/index.asp', 'modelsearch/admin.asp', 'admincontrol/login.asp', 'adm/admloginuser.asp', 'admloginuser.asp', 
		        'admin2/login.asp', 'admin2/index.asp', 'adm/index.asp', 'adm.asp', 'affiliate.asp', 'adm_auth.asp', 'memberadmin.asp', 
		        'administratorlogin.asp', 'siteadmin/login.asp', 'siteadmin/index.asp', 'ADMIN/', 'paneldecontrol/', 'login/', 'cms/', 'admon/',
		         'ADMON/', 'administrador/', 'ADMIN/login.php', 'panelc/', 'ADMIN/login.html', 'admin.', 'login.htm', 'login.', 
		         'admin/login.htm', 'admin/home.', 'admin/controlpanel.htm', 'admin/cp.', 'admin/adminLogin.htm', 'admin/admin_login.', 
		         'admin/controlpanel.', 'admin/admin-login.', 'admin-login.', 'admin/account.', 'admin/admin.', 'admin.htm', 'adminitem/', 
		         'adminitem.', 'adminitems/', 'adminitems.', 'administrator/login.', 'administrator.', 'administration.', 'adminlogin.', 
		         'admin_area/admin.', 'admin_area/login.', 'manager/', 'manager.', 'letmein/', 'letmein.', 'superuser/', 'superuser.', 'access/', 
		         'access.', 'sysadm/', 'sysadm.', 'superman/', 'supervisor/', 'panel.', 'control/', 'control.', 'member/', 'member.', 'members.', 
		         'user/', 'user.', 'cp/', 'uvpanel/', 'manage/', 'manage.', 'management/', 'management.', 'signin/', 'signin.', 'log-in/', 
		         'log-in.', 'log_in/', 'log_in.', 'sign_in/', 'sign_in.', 'sign-in/', 'sign-in.', 'users/', 'users.', 'accounts/', 'accounts.', 
		         'bb-admin/login.', 'bb-admin/admin.', 'administrator/account.', 'relogin.htm', 'relogin.html', 'check.', 'relogin.', 
		         'blog/wp-login.', 'user/admin.', 'users/admin.', 'registration/', 'processlogin.', 'checklogin.', 'checkuser.', 'checkadmin.', 
		         'isadmin.', 'authenticate.', 'authentication.', 'auth.', 'authuser.', 'authadmin.', 'cp.', 'modelsearch/login.', 'moderator.', 
		         'controlpanel.', 'admincontrol.', 'adminpanel.', 'fileadmin.', 'sysadmin.', 'admin1.', 'admin1.htm', 'admin2.', 'yonetim.', 
		         'yonetici.', 'ur-admin. Server.', 'administr8.', 'webadmin.', 'admins.', 'adm.', 'admin_login.', 'panel-administracion/login.', 
		         'pages/admin/admin-login.', 'pages/admin/', 'acceso.', 'admincp/login.', 'admincp/', 'admincontrol/', 'affiliate.', 'adm_auth.', 
		         'memberadmin.', 'administratorlogin.', 'modules/admin/', 'administrators.', 'siteadmin/', 'siteadmin.', 'adminsite/', 'kpanel/', 
		         'vorod/', 'vorod.', 'vorud/', 'vorud.', 'adminpanel/ PSUser/', 'secure/', 'webmaster.', 'autologin.', 'userlogin.', 'admin_area.', 
		         'cmsadmin.', 'security/', 'usr/', 'root/', 'secret/', 'admin/login.', 'admin/adminLogin.', 'moderator/login.', 
		         'moderator/admin. 0admin/ 0manager/', 'aadmin/', 'cgi-bin/login', 'login1', 'login_admin/', 'login_admin', 'login_out/', 
		         'login_out', 'login_user', 'loginerror/', 'loginok/', 'loginsave/', 'loginsuper/', 'loginsuper', 'login', 'logout/', 'logout', 
		         'secrets/', 'super1/', 'super1', 'super_index', 'super_login', 'supermanager', 'superman', 'superuser', 'supervise/', 
		         'supervise/Login super', 'admin.%EXT%', 'login.%EXT%', 'login/', 'adm/', 'admin/', 'admincp/', 'modcp/', 'administrator.php/', 
		         'moderator.php/', 'cms/', 'admin/account.%EXT%', 'admin/login.%EXT%', 'admin/home.%EXT%', 'admin/controlpanel.%EXT%',
		          'admin/cp.%EXT%', 'admin/adminLogin.%EXT%', 'admin/admin_login.%EXT%', 'admin/admin-login.%EXT%', 'admin-login.%EXT%',
		           'admin/admin.%EXT%', 'adminitem/', 'adminitem.%EXT%', 'adminitems/', 'adminitems.%EXT%', 'administrator/', 
		           'administrator/login.%EXT%', 'administrator.%EXT%', 'administration/', 'administration.%EXT%', 'adminLogin/', 
		           'adminlogin.%EXT%', 'admin_area/admin.%EXT%', 'admin_area/', 'admin_area/login.%EXT%', 'manager/', 'manager.%EXT%', 
		           'letmein/', 'letmein.%EXT%', 'superuser/', 'superuser.%EXT%', 'access/', 'access.%EXT%', 'sysadm/', 'sysadm.%EXT%', 'superman/', 
		           'supervisor/', 'panel.%EXT%', 'control/', 'control.%EXT%', 'member/', 'member.%EXT%', 'members/', 'members.%EXT%', 'user/', 
		           'user.%EXT%', 'cp/', 'uvpanel/', 'manage/', 'manage.%EXT%', 'management/', 'management.%EXT%', 'signin/', 'signin.%EXT%', 
		           'log-in/', 'log-in.%EXT%', 'log_in/', 'log_in.%EXT%', 'sign_in/', 'sign_in.%EXT%', 'sign-in/', 'sign-in.%EXT%', 'users/',
		            'users.%EXT%', 'accounts/', 'accounts.%EXT%', 'wp-login.php', 'bb-admin/login.%EXT%', 'bb-admin/admin.%EXT%', 'administrator/account.%EXT%', 
		            'relogin.%EXT%', 'check.%EXT%', 'blog/wp-login.%EXT%', 'user/admin.%EXT%', 'users/admin.%EXT%', 'registration/', 'processlogin.%EXT%',
		             'checklogin.%EXT%', 'checkuser.%EXT%', 'checkadmin.%EXT%', 'isadmin.%EXT%', 'authenticate.%EXT%', 'authentication.%EXT%', 
		             'auth.%EXT%', 'authuser.%EXT%', 'authadmin.%EXT%', 'cp.%EXT%', 'modelsearch/login.%EXT%', 'moderator.%EXT%', 'moderator/',
		              'controlpanel/', 'controlpanel.%EXT%', 'admincontrol.%EXT%', 'adminpanel.%EXT%', 'fileadmin/', 'fileadmin.%EXT%', 'sysadmin.%EXT%', 
		              'admin1.%EXT%', 'admin2.%EXT%', 'yonetim.%EXT%', 'yonetici.%EXT%', 'phpmyadmin/', 'myadmin/', 'ur-admin.%EXT%', 'ur-admin/', 
		              'Server.%EXT%', 'Server/', 'wp-admin/', 'administr8.%EXT%', 'administr8/', 'webadmin/', 'webadmin.%EXT%', 'administratie/',
		               'admins/', 'admins.%EXT%', 'administrivia/', 'Database_Administration/', 'useradmin/', 'sysadmins/', 'admin1/', 
		               'system-administration/', 'administrators/', 'pgadmin/', 'directadmin/', 'staradmin/', 'ServerAdministrator/', 'SysAdmin/',
		                'administer/', 'LiveUser_Admin/', 'sys-admin/', 'typo3/', 'panel/', 'cpanel/', 'cpanel_file/', 'platz_login/', 'rcLogin/',
		                 'blogindex/', 'formslogin/', 'autologin/', 'support_login/', '****_login/', 'manuallogin/', 'simpleLogin/', 'loginflat/', 
		                 'utility_login/', 'showlogin/', 'memlogin/', 'login-redirect/', 'sub-login/', 'wp-login/', 'login1/', 'dir-login/', 'login_db/',
		                  'xlogin/', 'smblogin/', 'customer_login/', 'UserLogin/', 'login-us/', 'acct_login/', 'bigadmin/', 'project-admins/', 
		                  'phppgadmin/', 'pureadmin/', 'sql-admin/', 'radmind/', 'openvpnadmin/', 'wizmysqladmin/', 'vadmind/', 'ezsqliteadmin/', 
		                  'hpwebjetadmin/', 'newsadmin/', 'adminpro/', 'Lotus_Domino_Admin/', 'bbadmin/', 'vmailadmin/', 'Indy_admin/', 'ccp14admin/', 
		                  'irc-macadmin/', 'banneradmin/', 'sshadmin/', 'phpldapadmin/', 'macadmin/', 'administratoraccounts/', 'admin4_account/', 
		                  'admin4_colon/', 'radmind-1/', 'Super-Admin/', 'AdminTools/', 'cmsadmin/', 'SysAdmin2/', 'globes_admin/', 'cadmins/', 
		                  'phpSQLiteAdmin/', 'navSiteAdmin/', 'server_admin_small/', 'logo_sysadmin/', 'power_user/', 'system_administration/', 
		                  'ss_vms_admin_sm/', 'bb-admin/', 'panel-administracion/', 'instadmin/', 'memberadmin/', 'administratorlogin/', 'adm.%EXT%', 
		                  'admin_login.%EXT%', 'panel-administracion/login.%EXT%', 'pages/admin/admin-login.%EXT%', 'pages/admin/', 'acceso.%EXT%', 
		                  'admincp/login.%EXT%', 'adminarea/', 'admincontrol/', 'affiliate.%EXT%', 'adm_auth.%EXT%', 'memberadmin.%EXT%', 
		                  'administratorlogin.%EXT%', 'modules/admin/', 'administrators.%EXT%', 'siteadmin/', 'siteadmin.%EXT%', 'adminsite/', 
		                  'kpanel/', 'vorod/', 'vorod.%EXT%', 'vorud/', 'vorud.%EXT%', 'adminpanel/', 'PSUser/', 'secure/', 'webmaster/', 
		                  'webmaster.%EXT%', 'autologin.%EXT%', 'userlogin.%EXT%', 'admin_area.%EXT%', 'cmsadmin.%EXT%', 'security/', 'usr/', 'root/', 
		                  'secret/', 'moderator/login.%EXT%', 'moderator/admin.%EXT%', '0admin/', '0manager/', 'aadmin/', 'cgi-bin/login%EXT%', 
		                  'login1%EXT%', 'login_admin/', 'login_admin%EXT%', 'login_out/', 'login_out%EXT%', 'login_user%EXT%', 'loginerror/', 'loginok/',
		                   'loginsave/', 'loginsuper/', 'loginsuper%EXT%', 'login%EXT%', 'logout/', 'logout%EXT%', 'secrets/', 'super1/', 'super1%EXT%', 
		                   'super_index%EXT%', 'super_login%EXT%', 'supermanager%EXT%', 'superman%EXT%', 'superuser%EXT%', 'supervise/', 
		                   'supervise/Login%EXT%', 'super%EXT%']
		urlopen = urllib.request.urlopen(url)
		cpfound = []
		num = 0
		numlist = 0
		numrang = 1086
		numm = 1086
		for i in CpAdminList:
			numlist+=1
			numm-=1
			CPUrl = url + i
			try:
				openCPUrl = urllib.request.urlopen(CPUrl)
				num+=1
				print("["+ str(numlist)+":"+str(numm)+":"+str(numrang)+"]" + CPUrl + "	Fount")
				cpfound.append(CPUrl)
				if save != None:
					saveurl = open(save,"+a")
					saveurl.write(str(num)+") "+CPUrl)
					saveurl.write("\n")
			except urllib.error.HTTPError as msgE:
				if error == "1":
					print("["+ str(numlist)+":"+str(numm)+":"+str(numrang)+"]" + CPUrl + " ::: Not Fount ::Error::",msgE)
				else:
					print("["+ str(numlist)+":"+str(numm)+":"+str(numrang) +"]" + CPUrl + " Not Fount")
				num+=1
				if esave != None:
					saveurl = open(esave,"+a")
					saveurl.write(str(num)+") "+CPUrl)
					saveurl.write("\n")
		print("")
		print("##########################[Cpanel Found]#######################")
		print("")
		if len(cpfound) > 0:
			num = 0 
			for i in cpfound:
				num = num + 1
				num = str(num)
				print(num+") "+ i)
				num = int(num)
			print("")
		else:
			print("Not FOund Url")

	except urllib.request.URLError as msgE:
		print(msgE)
else:
	print("""
CpAdmin.py [Options]
--------------------
-u      Url WebSite Search Cpanel Admin
-e      Shwo Error Url Not Found run -e 1
-S      Save Url Not Found  -S Name File
-s      Save Url Fount Cpanel Admin -s name File

Example:
	CpAdmin.py -u http://www.example.com/ add options 

		""")
