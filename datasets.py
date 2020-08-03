
# datasets needed for every cleaning processes

# for the code most_frequent_words_analyzer.py
### introduction code + cleaning code
stopwords_nt = {'we', 'ireland', 'scotland', 'australia', 'uk', 'wales', 'europe', 'world', 'france', 'germany',
                 'italy', 'spain', 'usa', 'portugal', 'denmark', 'netherlands', 'sweden', 'states', 'ue', 'england', 'kingdom',
                'norway', 'belgium', 'london', 'northern', 'southern','south', 'north'}

stopwords_year = {'1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997',
                  '1998', '1999', '2000',
                  '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012',
                  '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020'}

stopwords_vebs = {"'ve", "'re", "'d", "'s", "yet", "please", "since", "already", "every", "can", "could", "be", "have",
                  'rather',
                  'put', 'commonly', 'give', 'best', 'got', 't-shirt', 'month', 'height', 'shirt', 'delivery', 'team',
                  'experience', 'staff',
                  'advice', 'providing', 'talk', 'mean', 'u', 'per', 'latest', 'script', 'privacy'}

stopwords_lore_ipsum = {'Lorem', 'ipsum', ' dolor', ' sit', ' amet', ' consectetur', ' adipiscing', ' elit', ' sed',
                        'eiusmod', ' tempor', ' incididunt', ' ut',
                        ' labore', ' et ', 'dolore ', 'magna ', 'aliqua', 'elementum', ' pulvinar', ' etiam', ' non',
                        ' quam', ' Nisl', ' nisi', ' scelerisque',
                        'ltrices', ' vitae', ' auctor', 'Vel', ' orci', ' porta', 'pulvinar', ' Sollicitudin', ' nibh'}

stopwords_JV_HTML = {'ul', 'il', 'li', 'first-child', 'last-child', 'article', 'medium', 'div', 'form', 'tr', 'input',
                     'select', 'fieldset',
                     'icon', 'h2', 'header', 'th', 'color', 'h4', 'h5', 'h1', 'h0', 'width', 'var', 'ol', 'dm', 'dl',
                     'default', 'svg', '2', '3', '4', 'new',
                     'length', 'height', '1st', 'button', 'step', 'null', 'u', '1', 'thead', 'active', '5', '6', '7',
                     '8', '9', 'content', 'small', 'none',
                     'footer', 'footnote', 'dynamic', 'view', 'read', 'right', 'left', 'e', 'jquery', 'http', 'https',
                     'page', 'pagination', 'rtcommonprops', 'nav',
                     'dd', 'site', 'return', 'none', 'multiple', 'o', 'a', 'i', 'classic', 'year', 'true', 'rtl', 'h6',
                     'ffffff', 'n', 'url', 'lvl', 'time',
                     'day', 'cdata', 'contact', 'end', 'health', 'body', 'src', 'format', 'iefix', 'body', 'top',
                     'false', 'true', 'r', 'local', 'woff', 'truetype', 'eot',
                     'html', 'background', 'annum', 'j', 'x', 'start', 'type', 'help', 'ie', 'f', 'lable', '60',
                     'endif', 'manchester', 'home', 'website', 'posted', 'woff2',
                     'policy', '700', '1920', '1980', 'textarea', 'screen', 'asap', '020', 'h', 'checkbox', 'cooky',
                     'dt', 'w', 'submit', '400', 'italic', 'bold',
                     'keyframes', 'single', 'window', 'else', 'need', 'get', 'use', '100', 'apply', 'main', 'b', 'band',
                     'would', 'one', 'accordian', ' sit', 'debug',
                     'layout', 'nh', 'sidebar', 'image', 'propertyquery'}


stopwords_extra = {"0", "span", 'style=color', 'style=color', 'style=white-space', 'p', 'rgba', 'rgb', '51', 'pre-wrap',
                   '50', 'serf', 'background-color', '255', '256', '1500',
                   "'woff", "cooky", 'west', 'ga', 'l', 'sketch', 'radio', 'bounce40', 'href', 'lsdexception',
                   'blockquote', 'padding', 'ctimeline', 'plugin', 'wrapper', 'detail', 'head', 'normal',
                   'hover', 'function', 'disabled', 'td', 'tbody', 'important', 'focus', 'h3', 'figure', 'tfoot',
                   'img', 'aside', 'gdpr-dashboard', 'gdpr', 'dashboard', 'structure', 'icon', 'section', 'bordered',
                   'content'}

### URL - NAMES words divided by company type ###  CODE score_name_url.py

recruitment_title_words = ['job', 'hr', 'recruit', 'apprentice', 'placement', 'rec', 'employment', 'employ']
isv_title_words = ['.io', '.ai', 'digital', 'game', 'apps', 'information', 'technolog', 'studio', 'programming',
                   'software', 'tech', 'soft']
telco_title_words = ['tel', 'communication', 'talk', 'phone', 'network', 'tech', 'internet', 'wifi', 'mobile',
                     'broadband', 'fibre']
vendor_title_words = ['electronics', 'elec', 'data', 'tech', 'software', 'soft']
cloud_title_words = ['cyber', 'cloud', '.io', 'tech', 'consult', 'data', 'software', 'soft']
MSP_title_words = ['cloud', 'virtual', 'virt', 'tel', 'tech', 'soft', 'server', 'host', 'data', 'network', 'soft']
MS_title_words = ['it', 'data', 'tel', 'host', 'cyber', 'web', 'tech', 'internet', 'smart', 'soft']
DA_title_words = ['digital', 'web', 'influence', 'soft', 'internet', 'social', 'smart', 'data', 'media', 'creat',
                  'tel', 'tech', 'seo', 'design', 'agency']
RS_title_words = ['tech', 'virt', 'net', 'internet', 'compu', 'it', 'data', 'soft', 'web']
DS_title_words = ['tech', 'virt', 'net', 'internet', 'compu', 'it', 'data', 'soft', 'web']
OS_title_words = ['tech', 'virt', 'net', 'internet', 'compu', 'it', 'data', 'soft', 'web']

##### INTRO - SIC divided common words  for code SCORE_INTRO_SIC_CODES.py #####

# recruitment added
pool_recruitment_0 = ['recruitment', 'job', 'service', 'recruiter']  # 78200
pool_recruitment_1 = ['recruitment', 'job', 'service', 'recruiter']  # 78109  # no big difference

# ISV
pool_isv_0 = ['game', 'development', 'software', 'developer', 'independent', 'vendor']  # sic 62011

pool_isv_1 = ['software', 'solution', 'management', 'business', 'data', 'service', 'technology',
                'product', 'system', 'independent', 'vendor']  # sic 62012

pool_isv_2 = ['solution', 'data', 'software', 'service', 'management', 'company', 'business',
                'technology', 'platform', 'enterprise', 'client', 'help', 'independent', 'vendor']  # sic 62090

pool_isv_3 = ['software', 'solution', 'business', 'data', 'technology', 'service', 'company',
                'platform', 'system', 'management', 'help', 'independent', 'vendor']  # sic 62020
#### vendors
pool_vendor_0 = ['security', 'solution', 'business', 'data', 'software', 'virtualization', 'vendor',
                'technology', 'cloud', 'secure', 'product', 'management', 'network', 'iot']  # sic 62012

pool_vendor_1 = ['solution', 'security', 'business', 'data', 'technology', 'software', 'vendor',
                'management', 'network', 'cloud', 'information', 'access', 'virtualization',
                'platform', 'iot']  # sic 62020

pool_vendor_2 = ['solution', 'data', 'security', 'business', 'service', 'technology', 'vendor',
                'cloud', 'network', 'system', 'platform', 'virtualization', 'management', 'global', 'software',
                'performance', 'iot']  # sic 62090

### CLOUD CONSULTANT
pool_cloud_0 = ['business', 'solution', 'service', 'cloud', 'technology', 'cloudconsultant',
                'management', 'partner', 'microsoft', 'application', 'client', 'data']  # 62012

pool_cloud_1 = ['business', 'cloud', 'service', 'solution', 'technology', 'data', 'microsoft', 'support',
                'cloudconsultant',
                'partner', 'help', 'client', 'consultancy', 'management', 'enterprise', 'sharepoint']  # 62020

pool_cloud_2 = ['business', 'solution', 'service', 'cloud', 'microsoft', 'partner', 'cloudconsultant',
                'technology', 'google', 'data', 'management', 'client', 'help', 'organisation', 'network']  # 62090

### MSP ####
pool_msp_0 = ['service', 'business', 'solution', 'support', 'cloud', 'technology', 'security','managed', 'hosting', 'data',
                 'cyber', 'managed', 'service', 'provider']  # 62020

pool_msp_1 = ['service', 'business', 'cloud', 'solution', 'support', 'data', 'managed', 'service', 'provider',
                 'hosting', 'provider', 'technology', 'managed', 'security', 'network']  # 62090

# Managed services + telco
pool_ms_0 = ['service', 'business', 'solution', 'cloud', 'provider', 'managed', 'service',
                 'communication', 'network', 'data', 'technology', 'connectivity', 'managed']

pool_ms_1 = ['hosting', 'service', 'cloud', 'business', 'solution', 'data','managed', 'server', 'support', 'web']


pool_ms_2 = ['service', 'business', 'cloud', 'solution', 'support', 'data',
                 'hosting', 'provider', 'technology', 'managed', 'security', 'network', 'cyber']

# telco
pool_telco_0 = ['service', 'business', 'solution', 'communication', 'network', 'telecom', 'mobile',
                 'provider', 'call', 'voice', 'data', 'technology', 'broadband', 'telco',
                 'telecommunication']  # telco 61100


pool_telco_1 = ['service', 'business', 'network', 'solution', 'communication', 'telco', 'telecommunication',
                 'telecom', 'provider', 'mobile', 'technology', 'broadband']  # telco 61900

# digital agency
pool_da_0 = ['design', 'web', 'development', 'website', 'digital','agency', 'marketing', 'seo', 'online']  # DA 62012

pool_da_1 = ['design', 'web', 'development', 'website', 'digital','agency', 'marketing', 'seo', 'online', 'service']  # DA 62020

pool_da_2 = ['design', 'web', 'development', 'website', 'digital', 'marketing']  # DA 62020

pool_da_3 = ['design', 'web', 'development', 'website', 'digital', 'marketing', 'seo', 'brand', 'creative','content',
                 'social', 'graphic']  # DA 62090

# distributor
pool_distributor_0 = ['technology', 'product', 'distributor', 'market', 'solution', 'offer', 'supply']  # DS 46510

pool_distributor_1 = ['partner', 'distributor', 'distribution', 'market', 'supply']  # DS 62090

# Reseller
pool_reseller_0 = ['solution', 'service', 'technology', 'network', 'software', 'reseller']  # RS 62090

pool_reseller_1 = ['solution', 'service', 'technology', 'network', 'software', 'reseller']  # RS 62020

pool_reseller_2 = ['solution', 'service', 'technology', 'network', 'software', 'reseller']  # RS 62012

pool_reseller_3 = ['solution', 'service', 'technology', 'network', 'software', 'hardware', 'reseller']  # RS 46510

# outsorcer
pool_outsourcer_0 = ['outsourcing', 'management', 'service', 'support', 'organisation', 'technical', 'network', 'software',
                 'hardware', 'outsourcer']  # RS 46510

pool_outsourcer_1 = ['solution', 'management', 'service', 'organisation', 'technical', 'network', 'software', 'hardware',
                 'outsourcer']  # RS 46510

pool_outsourcer_2 = ['solution', 'management', 'organisation', 'service', 'technical', 'network', 'software', 'hardware',
                 'outsourcer']  # RS 46510

pool_outsourcer_3 = ['solution', 'management', 'organisation', 'service', 'technical', 'network', 'software', 'hardware',
                 'outsourcer']  # RS 46510

###################################################################################################################################

# score_web_text pool words

pool_words_R_ext = ['job', 'recruitment', 'candidate', 'service', 'client', 'manager', 'permanent', 'work', 'find',
                    'consultant', 'document',
                    'vacancy', 'hr', 'search', 'working', 'role', 'professional', 'career', 'opportunity']

pool_words_I_ext = ['service', 'management', 'customer', 'data', 'support', 'product', 'business', 'learn', 'google',
                    'information', 'cloud',
                    'digital', 'industry', 'market', 'game', 'tool', 'integration', 'financial', 'play', 'intelligence',
                    'blockchain', 'machine',
                    'intelligence', 'artificial', 'royalty', 'independent', 'software']

# distributor
pool_words_DS_ext = ['distributor', 'distribution', 'accessory', 'supply', 'management', 'sale', 'brand', 'cloud',
                     'network']

# outsourcer

pool_words_OS_ext = ['solution', 'service', 'support', 'customer', 'technology', 'network', 'software', 'provide',
                     'hardware', 'outsourer', 'outsourcing']

# Reseller
pool_words_RS_ext = ['cloud', 'technology', 'infrastructure', 'server', 'industry', 'cyber', 'consultancy', 'sell',
                     'vendor', 'hardware', 'storage', 'reseller', 'account']

# Digital Agency
pool_words_DA_ext = ['design', 'marketing', 'web', 'digital', 'seo', 'development', 'agency', 'online', 'social',
                     'website', 'project', 'brand', 'strategy',
                     'blog', 'creative', 'analytics', 'wordpress', 'hosting', 'video', 'ecommerce', 'branding',
                     'software', 'create', 'sale', 'advertising', 'digitalagency']

# MSP
pool_words_MSP_ext = ['support', 'translate', 'data', 'managed', 'security', 'hosting', 'network', 'server',
                      'management', 'learn', 'infrastructure', 'transform',
                      'digital', 'technical', 'provider', 'connectivity', 'domain', 'analytics', 'backup', 'hosted',
                      'recovery', 'services']

# CloudConsultant

pool_words_CC_ext = ['cloud', 'data', 'management', 'analytics', 'security', 'azure', 'microsoft', 'consultancy', 'aws',
                     'consulting', 'web', 'asc', 'server', 'cloudconsultant']

# Managed services

pool_words_MS_ext = ['managed', 'service', 'network', 'office', 'management', 'software', 'consultancy', 'resource',
                     'server', 'technology', 'digital']

# vendor
pool_words_VD_ext = ['software', 'digital', 'industry', 'global', 'technology', 'threat', 'value', 'protection',
                     'performance', 'sale', 'insight', 'host', 'account',
                     'press', 'advanced', 'machine', 'vendor']

# telco
pool_words_TC_ext = ['network', 'mobile', 'call', 'communication', 'broadband', 'navigation', 'cloud', 'tv', 'voice',
                     'provider', 'fibre', 'telephone', 'setting'
                                                       'software', 'telecommunication', 'telco']
### ENDUSER SIC CODES ### CODE sic_code_score.py
enduser_sic_codes = {1110.0, 1130.0, 1160.0, 1190.0, 1220.0, 1230.0, 1240.0, 1250.0, 1280.0, 1290.0, 1300.0, 1410.0, 1420.0, 1430.0, 1440.0, 1450.0,
                     1460.0, 1490.0, 1500.0, 1621.0, 1629.0, 1630.0, 1640.0, 1700.0, 2100.0, 2200.0, 2300.0, 3120.0, 3210.0, 3220.0, 5101.0, 5102.0,
                     7100.0, 8110.0, 8120.0, 8910.0, 8930.0, 10110.0, 10120.0, 10130.0, 10200.0, 10310.0, 10390.0, 10410.0, 10512.0, 10519.0, 10520.0,
                     10612.0, 10710.0, 10720.0, 10730.0, 10821.0, 10822.0, 10831.0, 10832.0, 10840.0, 10850.0, 10860.0, 10910.0, 11010.0, 11020.0, 11030.0,
                     11040.0, 11050.0, 11070.0, 12000.0, 13100.0, 13200.0, 13300.0, 13910.0, 13921.0, 13923.0, 13931.0, 13939.0, 13950.0, 13960.0, 13990.0,
                     14110.0, 14120.0, 14131.0, 14132.0, 14142.0, 15120.0, 15200.0, 16100.0, 16230.0, 16240.0, 16290.0, 17120.0, 17219.0, 17230.0, 18110.0,
                     18121.0, 18201.0, 18202.0, 19209.0, 20130.0, 20160.0, 20200.0, 20301.0, 20302.0, 20411.0, 20420.0, 20530.0, 20590.0, 20600.0, 21200.0,
                     22190.0, 22220.0, 22230.0, 22290.0, 23110.0, 23190.0, 23200.0, 23320.0, 23430.0, 23440.0, 23610.0, 23630.0, 23650.0, 23700.0, 23990.0,
                     24100.0, 24200.0, 24410.0, 24450.0, 24520.0, 25120.0, 25210.0, 25500.0, 25610.0, 25620.0, 25720.0, 25730.0, 25910.0, 25920.0, 25940.0,
                     26600.0, 26702.0, 27110.0, 27200.0, 27310.0, 27520.0, 28110.0, 28120.0, 28140.0, 28150.0, 28220.0, 28230.0, 28301.0, 28302.0, 28410.0,
                     28490.0, 28921.0, 28940.0, 28960.0, 29201.0, 29203.0, 29320.0, 30110.0, 30120.0, 30200.0, 30910.0, 30920.0, 31020.0, 32120.0, 32300.0,
                     32500.0, 33160.0, 35110.0, 35120.0, 35130.0, 35140.0, 35210.0, 35220.0, 35230.0, 37000.0, 38120.0, 38210.0, 38220.0, 38310.0, 42130.0,
                     42210.0, 42910.0, 43110.0, 43330.0, 43342.0, 43910.0, 43991.0, 45310.0, 45400.0, 46110.0, 46120.0, 46130.0, 46150.0, 46220.0, 46230.0,
                     46310.0, 46320.0, 46330.0, 46341.0, 46342.0, 46350.0, 46360.0, 46370.0, 46390.0, 46450.0, 46470.0, 46480.0, 46491.0, 46610.0, 46620.0,
                     46630.0, 46711.0, 46730.0, 46750.0, 46770.0, 47210.0, 47220.0, 47230.0, 47240.0, 47260.0, 47290.0, 47300.0, 47430.0, 47510.0, 47520.0,
                     47530.0, 47591.0, 47610.0, 47630.0, 47710.0, 47721.0, 47722.0, 47741.0, 47749.0, 47750.0, 47781.0, 47782.0, 47791.0, 47799.0, 47810.0,
                     47820.0, 49100.0, 49311.0, 49319.0, 49320.0, 49390.0, 50100.0, 50200.0, 51101.0, 51210.0, 51220.0, 52101.0, 52211.0, 52212.0, 52213.0,
                     52241.0, 52242.0, 55100.0, 55201.0, 55202.0, 55300.0, 56301.0, 58130.0, 58141.0, 59131.0, 59140.0, 64201.0, 64202.0, 64203.0, 64301.0,
                     64305.0, 64306.0, 65110.0, 65300.0, 68202.0, 69101.0, 71112.0, 74203.0, 75000.0, 77210.0, 77299.0, 77310.0, 77341.0, 77342.0, 77351.0,
                     77400.0, 79120.0, 79901.0, 81100.0, 81210.0, 81221.0, 81223.0, 81229.0, 81291.0, 81299.0, 81300.0, 82301.0, 82912.0, 82920.0, 84130.0,
                     84210.0, 84220.0, 84240.0, 84250.0, 85200.0, 85421.0, 85422.0, 85510.0, 85530.0, 88910.0, 90010.0, 91011.0, 91012.0, 91020.0, 91030.0,
                     91040.0, 93110.0, 93120.0, 93191.0, 93210.0, 94200.0, 94910.0, 94920.0, 95120.0, 95210.0, 95220.0, 95230.0, 95240.0, 95250.0, 95290.0,
                     96010.0, 96030.0, 97000.0, 98200.0, 99000.0}
