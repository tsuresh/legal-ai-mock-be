from flask import Flask, request, jsonify
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample question-answer pairs for each endpoint (replace with your actual data)
no_rag_data = [
    "This is a random answer for the /no_rag endpoint.",
    "Here's another possible response from /no_rag.",
]

auto_rag_data = [
    "This is a sample answer for the /auto_rag endpoint.",
    "Another random response from /auto_rag may go here.",
]

hil_rag_query_data = [
    "A humorous response could be displayed here for /hil_rag_query.",
    "This endpoint might provide a witty reply for /hil_rag_query.",
]


def get_random_answer(data):
    """Chooses a random answer from the provided data list."""
    return random.choice(data)


@app.route('/no_rag', methods=['POST'])
def no_rag():
    """Handles POST requests to the /no_rag endpoint."""
    question_data = request.get_json()
    if question_data is None:
        return jsonify({'error': 'Missing question data in JSON body'}), 400

    answer = get_random_answer(no_rag_data)
    return jsonify({'response': answer})


@app.route('/auto_rag', methods=['POST'])
def auto_rag():
    """Handles POST requests to the /auto_rag endpoint."""
    question_data = request.get_json()
    if question_data is None:
        return jsonify({'error': 'Missing question data in JSON body'}), 400

    answer = get_random_answer(auto_rag_data)
    return jsonify({'response': answer})


@app.route('/hil_rag_query', methods=['POST'])
def hil_rag_query():
    """Handles POST requests to the /hil_rag_query endpoint."""
    question_data = request.get_json()
    if question_data is None:
        return jsonify({'error': 'Missing question data in JSON body'}), 400

    answer = get_random_answer(hil_rag_query_data)
    return jsonify({'response': answer})


@app.route('/hil_rag', methods=['POST'])
def hil_rag():
    return jsonify({
        "casename": "Rule 7",
        "caseyear": "2008",
        "metadata": {
            "courtDetails": {
                "courtName": "Supreme Court of the Democratic Socialist Republic of Sri Lanka",
                "caseType": "S.C. (FR) Application",
                "caseNumber": "391",
                "caseYear": "2009"
            },
            "partiesInvolved": {
                "plaintiffs": [
                    {
                        "name": "Walawe Durage Dulani",
                        "address": "No. 323, Olcott Mawatha, Galle",
                        "role": "Petitioner"
                    }
                ],
                "defendants": [
                    {
                        "name": "Nimal Bandara",
                        "address": "Secretary, Ministry of Education, Isurupaya, Battaramulla",
                        "role": "1st Respondent"
                    },
                    {
                        "name": "H.A.K.R. Tissera",
                        "address": "Additional Secretary, Ministry of Education, Isurupaya, Battaramulla",
                        "role": "2nd Respondent"
                    },
                    {
                        "name": "Susil Premjayanth",
                        "address": "Minister of Education, Isurupaya, Battaramulla",
                        "role": "3rd Respondent"
                    },
                    {
                        "name": "H.H.A. Amarabandu",
                        "address": "No. 53, New City, Gonamulla",
                        "role": "4th Respondent"
                    },
                    {
                        "name": "H.N.D. Jayamaha",
                        "address": "Teacher Educator, Siyanae National College of Education, Veyangoda",
                        "role": "5th Respondent"
                    },
                    {
                        "name": "U.G.N. Kumari",
                        "address": "\u2018Sampath\u2019, Udumalagala, Nakiyadeniya",
                        "role": "6th Respondent"
                    },
                    {
                        "name": "University Grants Commission",
                        "address": "No. 20, Ward Place, Colombo 07",
                        "role": "7th Respondent"
                    },
                    {
                        "name": "Secretary, Public Service Commission",
                        "address": "No. 356 B, Carlwil Place, Colombo 03",
                        "role": "8th Respondent"
                    },
                    {
                        "name": "Hon. The Attorney-General",
                        "address": "Attorney General\u2019s Department, Colombo 12",
                        "role": "9th Respondent"
                    }
                ]
            },
            "judicialPanel": [
                {
                    "judgeName": "Dr. Shirani A. Bandaranayake",
                    "judgeTitle": "Judge of the Supreme Court"
                },
                {
                    "judgeName": "N.G. Amaratunga",
                    "judgeTitle": "Judge of the Supreme Court"
                },
                {"judgeName": "K. Sripavan", "judgeTitle": "Judge of the Supreme Court"}
            ],
            "counselDetails": [
                {
                    "forParty": "Petitioner",
                    "counselNames": ["Viran Corea", "S. Gunaratne"]
                },
                {
                    "forParty": "1st - 3rd and 7th - 9th Respondents",
                    "counselNames": ["S. Barrie, SC"]
                }
            ],
            "hearingDetails": {
                "hearingDates": ["31.05.2010"],
                "decisionDate": "31.01.2011",
                "writtenSubmissions": [
                    {"party": "Petitioner", "date": "07.07.2010"},
                    {"party": "Respondents", "date": "11.10.2010"}
                ]
            },
            "judgmentDetails": {
                "issuedBy": "Dr. Shirani A. Bandaranayake",
                "outcome": "Dismissed",
                "judgmentSummary": "The petitioner had not been successful in establishing that the respondents had violated her fundamental right guaranteed in terms of Article 12(1) of the Constitution."
            }
        }
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)