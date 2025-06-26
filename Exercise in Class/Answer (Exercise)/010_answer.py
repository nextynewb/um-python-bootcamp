salaries = {
    "name": "Salaries Data for Software Engineer",
    "data": [
        {
            "company_name": "ViewSoft",
            "company_score": 4.8,
            "position": "Software Engineer",
            "location": "Manassas, VA",
            "pay": "$68K"
        },
        {
            "company_name": "KAIROS Inc",
            "company_score": 3.5,
            "position": "Software Engineer",
            "location": "Dahlgren, VA",
            "pay": "$6K"
        },
        {
            "company_name": "Topaz Labs",
            "company_score": 3.7,
            "position": "Senior Software Engineer - Photo AI",
            "location": "Dallas, TX",
            "pay": "$68K"
        },
        {
            "company_name": "S3",
            "company_score": 3.8,
            "position": "Software Engineer- 826245",
            "location": "Stennis Space Center, MS",
            "pay": "$56K"
        },
        {
            "company_name": "J. Paul Getty Trust, The",
            "company_score": 4.1,
            "position": "Software Engineer Sr",
            "location": "Los Angeles, CA",
            "pay": "$272K"
        },
        {
            "company_name": "Topaz Labs",
            "company_score": 3.4,
            "position": "Software Engineer - ML Performance / HPC",
            "location": "Dallas, TX",
            "pay": "$90K"
        },
        {
            "company_name": "Rover.com",
            "company_score": 3.2,
            "position": "Senior Software Engineer, Orders Team",
            "location": "Seattle, WA",
            "pay": "$101K"
        },
        {
            "company_name": "University of Oregon",
            "company_score": 3.8,
            "position": "Research Software Engineer",
            "location": "Eugene, OR",
            "pay": "$155K"
        },
        {
            "company_name": "d\u014dTERRA International",
            "company_score": 4.0,
            "position": "Software Engineer II",
            "location": "Utah",
            "pay": "$285K"
        },
        {
            "company_name": "AHU Technologies",
            "company_score": 4.6,
            "position": "Software Engineer",
            "location": "Newark, DE",
            "pay": "$130K"
        }
    ]
}


RATE = 4.4


for salary in salaries['data']:
    pay = salary['pay']
    pay = pay.replace('$', '').replace('K', '000').replace(',', '')
    pay = float(pay)
    if pay < 100000:
        salary['income_class'] = 'low'
    elif 100000 <= pay < 200000:
        salary['income_class'] = 'middle'
    elif 200000 <= pay < 300000:
        salary['income_class'] = 'high'

    salary['pay_in_usd'] = pay
    salary['pay_in_myr'] = pay * RATE

    print(salary)
    