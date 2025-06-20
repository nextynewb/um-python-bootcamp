"""
Exercise: Loop through the salaries data and print the company name, position, and pay.

Instructions:
    1. Loop through the salaries data
    2. Convert the pay to pay_in_usd (use String manipulation) + (type cast to float)
    3. Convert the pay to pay_in_myr (pay_in_usd * 4.4)
    4. Add the income_class based on the pay_in_usd (low, middle, high)
        - low: < 100000
        - middle: 100000 <= pay < 200000
        - high: 200000 <= pay < 300000
    5. Add the pay_in_usd and pay_in_myr, `income_class` to the salary data


{
'company_name': 'ViewSoft',
'position': 'Software Engineer',
'pay': '$68K',
'pay_in_usd': 68000,
'pay_in_myr': 299200,
'income_class': 'high'
}

"""


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


# 1. Loop through the salaries data here