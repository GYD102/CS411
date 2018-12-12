class WinnerComputer:

    @staticmethod
    def get_sen_core_from_file(sen_code):
        tf = open(sen_code + ".txt", "r")
        ustr = tf.read()
        d = locals()
        tf.close()
        exec("f = " + ustr, globals(), d)
        return d['f']

    @staticmethod
    def comp(key, user_score, score_list, s1, s2):
        """
        :param key: str : one of the stances
        :param user_score: int : +1, 0, or -1 : what the user answered for stance key
        :param score_list: List of 2 values : first val is senator_1 score and second is senator_2 score
        :param s1: dict: senator_1's stances: val
        :param s2: dict: senator_2's stances: val
        :return: updated score_list
        """
        a = 0
        b = 0
        if key in s1.keys():
            a = s1[key]
            if a != 0:
                a = a / abs(a)
        if key in s2.keys():
            b = s2[key]
            if b != 0:
                b = b / abs(b)
        if user_score == a:
            score_list[0] += 1
        if user_score == b:
            score_list[1] += 1
        return score_list

    @staticmethod
    def compute_winner(senator_id_1, senator_id_2, user_scores):
        """
        :param senator_id_1: str
        :param senator_id_2: str
        :param user_scores: dict : d[stance : str] = val : int
        :return:
        """
        senator_stances_1 = WinnerComputer.get_sen_core_from_file(senator_id_1)
        senator_stances_2 = WinnerComputer.get_sen_core_from_file(senator_id_2)
        score_list = [0, 0]
        for topic in user_scores:
            score_list = WinnerComputer.comp(topic, user[topic], score_list, senator_stances_1, senator_stances_2)

        print(score_list)

        if score_list[0] > score_list[1]:
            return senator_id_1

        return senator_id_2


if __name__ == "__main__":
    s_id_1 = 'B001230'
    s_id_2 = 'B001261'
    user = {'Child health': 15, "Women's health": 33, 'Right of privacy': 9, 'Disability and paralysis': 17,
            'Aviation and airports': 4, 'Transportation programs funding': 10, 'Transportation and Public Works': 18,
            'Capital gains tax': 2, 'Tax administration and collection, taxpayers': 8, 'Income tax rates': 10,
            'Financial services and investments': 5, 'Accounting and auditing': 7, 'Taxation': 4,
            'Congressional agencies': 1, 'Library of Congress': 3, 'Government Accountability Office (GAO)': 0,
            'Congressional officers and employees': 4, 'Government employee pay, benefits, personnel management': 34,
            'Adoption and foster care': 9, 'Administrative law and regulatory procedures': 48,
            'National Guard and reserves': 15, 'Family relationships': 15, 'Office of Personnel Management (OPM)': 2,
            'Employee leave': 20, 'Government Operations and Politics': 58, 'Government trust funds': 16,
            'Land transfers': 7, 'Outdoor recreation': 2, 'Land use and conservation': 6,
            'Parks, recreation areas, trails': 5, 'Hunting and fishing': 3, 'Public Lands and Natural Resources': 7,
            'Supreme Court': 7, 'Constitution and constitutional amendments': 13,
            'Commemorative events and holidays': 52, 'Employment discrimination and employee rights': 25,
            'Sex, gender, sexual orientation discrimination': 63, 'Due process and equal protection': 9,
            'Housing discrimination': 8, 'Civil Rights and Liberties, Minority Issues': 41,
            'Department of the Interior': 0, 'Public lands and natural resources': 2, 'Currency': 3,
            'Congressional oversight': 27, 'Higher education': 53, 'Government information and archives': 64,
            'Education programs funding': 34, 'Child care and development': 18, 'Education': 47,
            'Science, Technology, Communications': 14, 'Congressional tributes': 36,
            'Disability and health-based discrimination': 16, "Veterans' education, employment, rehabilitation": 10,
            'World health': 7, 'Foreign aid and international relief': 5, 'Health promotion and preventive care': 17,
            'International organizations and cooperation': 9, 'Public participation and lobbying': 12,
            'International Affairs': 5, 'Department of Justice': 8, 'Criminal procedure and sentencing': 2,
            'Licensing and registrations': -2, 'Trade restrictions': 0, 'Criminal justice information and records': 23,
            'Firearms and explosives': 28, 'Law enforcement administration and funding': 22,
            'Retail and wholesale trades': 7, 'Crime and Law Enforcement': 20, 'Appropriations': 16,
            'Water quality': 19, 'Public contracts and procurement': 18, 'Energy efficiency and conservation': 5,
            'Consumer affairs': 6, 'Government lending and loan guarantees': 16, 'Solid waste and recycling': 3,
            'Water use and supply': 16, 'State and local finance': 6, 'Environmental Protection': 15,
            'Federal officials': 4, 'Government ethics and transparency, public corruption': 15,
            'Environmental Protection Agency (EPA)': 12, 'Housing and Community Development': 2, 'Small business': 5,
            'Department of the Treasury': 4, 'Securities': 4, 'Executive agency funding and structure': 33,
            'Employee benefits and pensions': 13, 'Income tax deferral': -1, 'Performance measurement': 7,
            'Computers and information technology': 11, 'Advisory bodies': 10,
            'Computer security and identity theft': 5, 'Europe': -3, 'Human rights': 9, 'Turkey': 0, 'Armenia': 1,
            'War crimes, genocide, crimes against humanity': 1, 'Israel': 3, 'Research and development': 8,
            'Middle East': -1, 'Research administration and funding': 20,
            'Technology transfer and commercialization': -1, 'Scientific communication': 1, 'Medical research': 17,
            'Health': 13, 'Corporate finance and management': 10,
            'Military procurement, research, weapons development': 2, 'Foreign and international corporations': 7,
            'Elementary and secondary education': 29, 'Educational facilities and institutions': 16,
            'Environmental assessment, monitoring, research': 11, 'Hazardous wastes and toxic substances': 11,
            'Environmental regulatory procedures': 7, 'Roads and highways': 6, 'Historic sites and heritage areas': 3,
            'Latin America': 9, 'Caribbean area': 4, 'Cuba': 1, 'Sanctions': -1, 'Agricultural trade': -1,
            'Foreign Trade and International Finance': 1, 'Air quality': 9, 'Climate change and greenhouse gases': 7,
            'Energy storage, supplies, demand': 1, 'Alternative and renewable resources': 2,
            'Electric power generation and transmission': 2, 'Motor fuels': 2, 'Lighting and heating': -2,
            'Congressional elections': 10, 'Elections, voting, political campaign regulation': 28,
            'Political parties and affiliation': 6, 'Preschool education': 7, 'School administration': 6,
            'State and local government operations': 39, 'Child safety and welfare': 16, 'Commuting': -2,
            'Transportation costs': 1, 'Pedestrians and bicycling': -2, 'Income tax exclusion': -2,
            'Inflation and prices': 11, 'Public transit': 5, 'Education of the disadvantaged': 12,
            'Student aid and college costs': 28, 'Teaching, teachers, curricula': 11, 'Income tax credits': 8,
            'Science and engineering education': 6, 'Drug trafficking and controlled substances': -3,
            'Health programs administration and funding': 6, 'Prescription drugs': -2, "Veterans' medical care": 2,
            'Alabama': 3, 'Armed forces and national security': -8, 'Health information and medical records': 4,
            "Veterans' pensions and compensation": 5, 'Health care coverage and access': 12,
            'Military facilities and property': 2, 'Medical tests and diagnostic methods': 4,
            'Disability assistance': 4, 'Armed Forces and National Security': 9, 'Religion': 15, 'Crime prevention': 7,
            'Administrative remedies': 16, 'Military personnel and dependents': 21, 'Racial and ethnic relations': 49,
            'Crimes against children': 10, 'Crime victims': 22, 'Assault and harassment offenses': 22,
            'Homelessness and emergency shelter': 12, 'Alliances': -1, 'Thailand': -2, 'Asia': 16,
            'Diplomacy, foreign officials, Americans abroad': 10, 'U.S. history': 20, 'Department of Defense': 13,
            'Military medicine': 0, 'Budget deficits and national debt': 2, 'Defense spending': 7, 'Violent crime': 21,
            'Domestic violence and child abuse': 19, 'Sex offenses': 13, 'Law enforcement officers': 14,
            'Department of State': 3, 'Hate crimes': 6, 'Refugees, asylum, displaced persons': 17,
            'Military education and training': 2, 'Subversive activities': 2, 'Russia': 3,
            'Congressional-executive branch relations': 2,
            'Intelligence activities, surveillance, classified information': 3,
            'Government studies and investigations': 20, 'Presidents and presidential powers, Vice Presidents': 14,
            'Motor vehicles': 2, 'Civil actions and liability': 56, 'Immigration status and procedures': 28,
            'Criminal investigation, prosecution, interrogation': 17, 'Citizenship and naturalization': 5,
            'Fraud offenses and financial crimes': 12, 'Food supply, safety, and labeling': 1,
            'Agricultural practices and innovations': 1, 'Horticulture and plants': 3,
            'Urban and suburban affairs and development': 6, 'Fruit and vegetables': 2, 'Agriculture and Food': -1,
            'Social Welfare': 8, 'Adult day care': 1, 'Long-term, rehabilitative, and terminal care': -3, 'Tariffs': -2,
            'Labor and Employment': 34, 'Watersheds': 3, 'Canada': 5, 'Great Lakes': 9,
            'Radioactive wastes and releases': 4, 'Medical education': 4, 'Nursing': 4, 'Aging': 2,
            'Health personnel': -2, 'Health facilities and institutions': 8, 'Commerce': -2, 'Railroads': 3,
            'Social Security Administration': 3, 'Wages and earnings': 27, 'Transportation employees': 3,
            'Employment taxes': 4, 'Social security and elderly assistance': 11, 'Pornography': 0,
            'Internet and video services': 2, 'Human trafficking': 6,
            'Animal protection and human-animal relationships': -3, 'Crimes against animals and natural resources': -5,
            'Television and film': -1, 'Photography and imaging': -1, 'Digital media': 1, 'Business records': 0,
            'Internal Revenue Service (IRS)': 6, 'Medicare': -19, 'Minority employment': 1, 'Hospital care': -2,
            'Minority health': 6, 'Product safety and quality': 3, 'Manufacturing': 7, 'Law': 14, 'Labor standards': 7,
            'Emergency medical services and trauma care': 4, 'First Amendment rights': 0,
            'First responders and emergency personnel': 7, 'Pennsylvania': 0, 'Environmental health': 10,
            'Philippines': 9, 'Immigration': 21, 'Protection of officials': 4, 'Virginia': 2,
            'House of Representatives': 14, 'Members of Congress': 7, 'Congressional leadership': 1, 'U.S. Capitol': 4,
            'Congress': 11, 'Poverty and welfare assistance': 2, 'Housing and community development funding': 4,
            'Low- and moderate-income housing': 3, 'Aquaculture': -2, 'Agriculture and food': -3,
            'Agricultural marketing and promotion': -2, 'Rural conditions and development': 11, "Women's rights": 11,
            'Minority education': 8, 'Area studies and international education': 2,
            'Foreign language and bilingual programs': 5, 'Department of Transportation': 6,
            'Transportation safety and security': 8, 'Service animals': 1, 'Access Board': 2, 'Government liability': 5,
            'Merit Systems Protection Board': 2, 'Marriage and family status': 16, 'Consumer credit': 2,
            'Finance and Financial Sector': 0, 'Detention of persons': 14, 'Organized crime': 0,
            'Intergovernmental relations': 11, 'Department of Homeland Security': 18,
            'Border security and unlawful immigration': 17, 'Terrorism': -6, 'Florida': 0, 'Iraq': -2,
            'Health care costs and insurance': 5, 'Mental health': 9, 'Emergency management': -1,
            'Legislative rules and procedure': 2, 'Disaster relief and insurance': 0, 'Floods and storm protection': 1,
            'Federal Emergency Management Agency (FEMA)': 2, 'Emergency planning and evacuation': -1,
            'Residential rehabilitation and home repair': 0, 'Emergency Management': 4, 'Postal service': 9,
            'U.S. Postal Service': 2, 'Department of Veterans Affairs': -2, 'Sex and reproductive health': 9,
            'Regional and metropolitan planning': 4, 'Neurological disorders': 1,
            'Hereditary and development disorders': -2, 'Home and outpatient care': 0, 'Budget process': 0,
            'U.S. and foreign investments': 0, 'Military history': 5, 'Personnel records': 7,
            'Evidence and witnesses': 13, 'Alaska': 6,
            'Wilderness and natural areas, wildlife refuges, wild rivers, habitats': 8,
            'Wildlife conservation and habitat protection': 5, 'Arctic and polar regions': 5,
            'Crimes against women': 10, 'Coast guard': 3, 'Military law': 0, 'Sales and excise taxes': 1,
            'Lawyers and legal services': 9, 'Conflicts and wars': 8, 'Marine and inland water transportation': 7,
            'Government buildings, facilities, and property': 16, 'Separation, divorce, custody, support': 7,
            'Judicial procedure and administration': 8, 'Visas and passports': 4, 'Mexico': 7,
            'International monetary system and foreign exchange': 1, 'U.S. Sentencing Commission': 0,
            'Drug, alcohol, tobacco use': 1, 'Correctional facilities and imprisonment': 7,
            'Federal district courts': 3, 'International law and treaties': -2, 'Cancer': 7, 'Marshall Islands': 2,
            'Nuclear weapons': -1, 'Radiation': 1, 'Department of Commerce': -3,
            'Advanced technology and technological innovations': 4,
            'Competitiveness, trade promotion, trade deficits': 0, 'Economics and public finance': -1,
            'Economics and Public Finance': -3, 'Medicaid': -3, 'Crime and law enforcement': -1, 'Livestock': 0,
            'Agricultural conservation and pollution': -1, 'Pollution liability': -1, 'Ukraine': -1,
            'Sovereignty, recognition, national governance and status': 4, 'Intellectual property': -3,
            'News media and reporting': 2, 'Marketing and advertising': 5, 'User charges and fees': 1,
            'Broadcasting, cable, digital technologies': 8, 'Iran': 0, 'Government operations and politics': 6,
            'Federal-Indian relations': 4, 'Voting rights': 11, 'Alaska Natives and Hawaiians': 3,
            'Indian lands and resources rights': 3, 'Legal fees and court costs': 6, 'Native Americans': 0,
            'Smithsonian Institution': 2, 'Museums, exhibitions, cultural centers': 5,
            "Veterans' organizations and recognition": 1, 'Federal Communications Commission (FCC)': 7,
            'Telephone and wireless communication': 12, 'Athletes': 7, 'Professional sports': 6, 'Illinois': 18,
            'Sports and Recreation': 7, 'Mammals': -5, 'Motor carriers': 4, 'Animals': -2, 'Japan': 0,
            'Drug therapy': 3, 'Business investment and capital': 1, 'Worker safety and health': 5,
            'Allied health services': 2, 'Customs enforcement': 4, 'Employee hiring': 12, 'Employee performance': 1,
            'Health technology, devices, supplies': -12, 'Cemeteries and funerals': 3, 'Building construction': 4,
            'Materials': -2, 'Judicial review and appeals': -3, 'Income tax deductions': 3,
            'Social work, volunteer service, charitable organizations': 8, 'Interest, dividends, interest rates': 12,
            'Judges': 7, 'European Union': 0, 'Norway': 1, 'Iceland': 1, 'Trade agreements and negotiations': 4,
            'Digestive and metabolic diseases': 0, 'Historical and cultural resources': 4,
            'Banking and financial institutions regulation': -6, 'Tax-exempt organizations': 4, 'Dental care': -1,
            'Senate': 0, 'Nevada': -1, 'Environmental technology': 3, 'Pipelines': -1, 'Energy': 7,
            'Life, casualty, property insurance': -3, 'Utah': 3, 'Emergency communications systems': 3,
            'Oil and gas': 8, 'Industrial facilities': 2, 'Music': 0, 'Federal preemption': 0, 'Sound recording': -1,
            'International affairs': -1, 'Department of Health and Human Services': -1, 'Political advertising': 4,
            'Business ethics': 2, 'Labor-management relations': 16, 'Credit and credit markets': 0,
            'Bank accounts, deposits, capital': -1, 'South Korea': -1, 'Foreign labor': -2,
            'Cultural exchanges and relations': 3, 'Community life and organization': 6, 'Families': 4,
            'Travel and tourism': 4, 'Tax treatment of families': 2, 'Food assistance and relief': 1,
            'Alcoholic beverages': 1, 'Public housing': 1, 'Unemployment': 10, 'Family planning and birth control': 6,
            'Census and government statistics': 5, 'Panama': -1, 'India': 0, 'District of Columbia': -2,
            'Mississippi': -1, 'Missouri': -1, 'New York State': 0, 'North Carolina': 0, 'South Carolina': 0,
            'Maryland': -1, 'Colorado': 0, "Veterans' loans, housing, homeless programs": -3,
            'Chemical and biological weapons': -1, 'Vocational and technical education': 6, 'Educational guidance': 2,
            'Arizona': 4, 'California': 8, 'Texas': 2, 'New Mexico': 3, 'Genetics': 3,
            'Insurance industry and regulation': -3, 'Environmental protection': -1,
            'Sports and recreation facilities': 3, 'Physical fitness and lifestyle': -1, 'Malaysia': 1,
            'Northern Mariana Islands': 7, 'Language arts': 2, 'Election Assistance Commission': 3,
            'U.S. territories and protectorates': 7, 'Employment and training programs': 21, 'Fires': 3,
            'United Nations': -2, 'North Korea': -1, 'War and emergency powers': 0, 'Metals': 3,
            'Rule of law and government transparency': 2, 'Smuggling and trafficking': 3,
            'Arms control and nonproliferation': -1, 'Crimes against property': -1,
            'Foreign and international banking': -3, 'International exchange and broadcasting': -2,
            'Protest and dissent': -1, 'Military assistance, sales, and agreements': 1, 'Foreign property': -3,
            'Real estate business': -1, 'Federal Reserve System': -4, 'National Credit Union Administration': -3,
            'Housing finance and home ownership': 0, 'Securities and Exchange Commission (SEC)': -1,
            'Federal Deposit Insurance Corporation (FDIC)': -4, 'Consumer Financial Protection Bureau': -4, 'Syria': 1,
            'Africa': 7, 'Sudan': 4, 'Somalia': 4, 'Libya': 4, 'Yemen': 4, 'Taxation of foreign income': 5,
            'Infrastructure development': 6, 'Transportation and public works': 1, 'Public-private cooperation': 2,
            'Government corporations and government-sponsored enterprises': 7, 'Puerto Rico': 1,
            'Forests, forestry, trees': 0, 'Nuclear power': 1, 'Hybrid, electric, and advanced technology vehicles': 2,
            'Department of Energy': 0, 'Water resources funding': 1, 'Minority and disadvantaged businesses': -2,
            'Cardiovascular and respiratory health': 5, 'State and local taxation': 0, 'Department of Agriculture': -2,
            'Veterinary medicine and animal diseases': -1, 'Monuments and memorials': -3,
            'Military operations and strategy': -1, 'Comprehensive health care': 0, 'Economic development': 10,
            'Coal': 2, 'Economic performance and conditions': 0, 'Mining': 5, "Women's employment": 6,
            'Arts, Culture, Religion': 4, 'Family services': 1, 'Indian social and development programs': 5,
            'Juvenile crime and gang violence': 4, 'Immigrant health and welfare': 3, 'Jurisdiction and venue': 2,
            'Marine and coastal resources, fisheries': 9, 'Palestinians': 2, 'Gaza Strip': 1,
            'Arab-Israeli relations': 1, 'Freedom of information': 2, 'National Archives and Records Administration': 0,
            'Alternative dispute resolution, mediation, arbitration': 4, 'Finance and financial sector': -3,
            'Congressional operations and organization': 2, 'Meat': -1, 'Social welfare': 1, 'Ethiopia': 1,
            'Michigan': 1, 'Special education': 4, 'Academic performance and assessments': 4, 'Nutrition and diet': 1,
            'Business education': 0, 'Small Business Administration': -1,
            'Drug safety, medical device, and laboratory regulation': 1, 'Public utilities and utility rates': 1,
            'Equal Employment Opportunity Commission (EEOC)': 4, 'Consumer Product Safety Commission': 1,
            'Adult education and literacy': 8, 'General Services Administration': 3,
            'Office of Management and Budget (OMB)': 5, 'Energy research': 2, 'Biological and life sciences': 2,
            'Tax reform and tax simplification': 1, 'Specialized courts': 5, 'Art, artists, authorship': 3,
            'Export-Import Bank of the United States': 2, 'Health care quality': -3, 'Labor and employment': 2,
            'Accidents': 4, 'Centers for Disease Control and Prevention (CDC)': 4, 'Gulf of Mexico': 2,
            'Atlantic Ocean': 2, 'Federal Bureau of Investigation (FBI)': 1, 'Montana': 1, 'Egypt': -1,
            'Congressional committees': 2, 'World history': 1, 'Congressional districts and representation': 3,
            'Temporary and part-time employment': 6, 'Civil rights and liberties, minority issues': 1,
            'Military civil functions': 0, 'Homeland security': 0, 'Debt collection': 2,
            'Housing supply and affordability': 1, 'New York City': 4, 'Musculoskeletal and skin diseases': 0,
            'China': 4, 'Presidential administrations': 2, 'Teenage pregnancy': 1,
            'Youth employment and child labor': 3, 'Women in business': -2, 'Virgin Islands': 4, 'American Samoa': 2,
            'Free trade and trade barriers': 2, 'Sexually transmitted diseases': 2, 'HIV/AIDS': 2, 'Afghanistan': -1,
            'Alternative treatments': -2, 'General energy matters': 1, 'Burma': 1,
            'Infectious and parasitic diseases': 2, 'Immunology and vaccination': 2,
            'Federal Election Commission (FEC)': 3, 'Hearing, speech, and vision care': -4,
            'Migrant, seasonal, agricultural labor': 4, 'Lebanon': -3, 'Space flight and exploration': 1,
            'Nebraska': -2, 'National Railroad Passenger Corporation (Amtrak)': 2, 'Fishes': 6, 'Bankruptcy': 0,
            'Libraries and archives': 3, 'Buy American requirements': 7, 'Noise pollution': 5,
            'Navigation, waterways, harbors': 2, 'General public lands matters': 2, 'Natural disasters': -1,
            'Nuclear Regulatory Commission (NRC)': -1, 'Strategic materials and reserves': -2, 'Ohio': 1, 'Oregon': 1,
            'Washington State': 1, 'Pacific Ocean': 1, 'Maine': 1, 'Hawaii': 3, 'National symbols': 2,
            'Educational technology and distance education': -2, 'National Aeronautics and Space Administration': 3,
            'Product development and innovation': -2, 'Trade secrets and economic espionage': -1,
            'Industrial policy and productivity': 1, 'Rhode Island': 1, 'Political movements and philosophies': 0,
            'Food industry and services': 1, 'Financial literacy': 2, 'Humanities programs funding': 1,
            'School athletics': 2, 'Executive Office of the President': 1, 'Soil pollution': 1,
            'National Institutes of Health (NIH)': -1, 'Charitable contributions': -3, 'Vocational education': -1,
            'Housing for the elderly and disabled': -1, 'National and community service': 4, 'Abortion': 5,
            'Contracts and agency': 7, 'Competition and antitrust': 3, 'National Science Foundation': 1,
            'Atmospheric science and weather': 1, 'Military readiness': 0, 'Agricultural prices, subsidies, credit': -1,
            'Lease and rental services': 2, 'Performing arts': 1, 'Technology assessment': 2, 'Guatemala': 1,
            'El Salvador': 1, 'Honduras': 1, "Women's education": 1, 'Vietnam': 2, 'South Africa': 1, 'Ireland': 1,
            'Nepal': 2, 'Tibet': 1, 'Oceania': 1, 'Hong Kong': 1, 'Guam': 1, 'Department of Labor': 6, 'Brazil': 1,
            'Micronesia': 1, 'Palau': 1, 'Espionage and treason': 1, 'Self-employed': 1,
            'Telecommunication rates and fees': 3, 'House Committee on Ethics': 1, 'Policy sciences': 1,
            'Senate Select Committee on Ethics': 1, 'Commodities markets': -2,
            'Corporation for National and Community Service': 2, 'Nigeria': 1, 'Energy revenues and royalties': 1,
            'Food and Drug Administration (FDA)': -1, 'Surgery and anesthesia': -1,
            'Commodity Futures Trading Commission': -1, 'Federal Housing Finance Agency': -1,
            'U.S. Agency for International Development (USAID)': 0, 'Kentucky': -1, 'Mississippi River': 1,
            'Aquatic ecology': 3, 'Lakes and rivers': 1, 'Dams and canals': 4, 'Water Resources Development': 1,
            'Germany': 1, 'Literature': 1, 'Belgium': -1, 'Arctic Ocean': 2, 'National Labor Relations Board (NLRB)': 3,
            'Social Sciences and History': 1, 'State and local courts': 1, 'Student records': 1, 'Property tax': -1,
            'Jordan': -1, 'Department of Education': 4, 'Kuwait': -1, 'Transfer and inheritance taxes': 0,
            'Venezuela': 1, 'Chad': 1, 'Energy prices': -1, 'Age discrimination': 1, 'Wetlands': 1, 'Kansas': -1,
            'Foreign trade and international finance': 1, 'Agricultural research': 0, 'Olympic games': -1,
            'New Jersey': 1, 'Marine pollution': 1, 'Foreign loans and debt': -1, 'Laos': 1, 'Medical ethics': -1,
            'Massachusetts': 2, 'Drug and radiation therapy': -1, 'Reptiles': -1,
            'Endangered and threatened species': -1, 'Pest management': -1, 'France': 1, 'Italy': 1,
            'Railroad Retirement Board': 1, 'Science, technology, communications': 1, 'Farmland': -1}

    print(WinnerComputer.compute_winner(s_id_1, s_id_2, user))
