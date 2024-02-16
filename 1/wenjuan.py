from flask import Flask, request, jsonify

app = Flask(__name__)

# 用于存储问卷数据的列表
survey_data = []

@app.route('/submit_survey', methods=['POST'])
def submit_survey():
    # 获取提交的问卷数据
    data = request.get_json()

    # 将问卷数据添加到列表中
    survey_data.append(data)

    # 返回成功信息
    return jsonify({"message": "Survey submitted successfully!"}), 200

@app.route('/get_survey_data', methods=['GET'])
def get_survey_data():
    # 返回所有问卷数据
    return jsonify(survey_data), 200

if __name__ == '__main__':
    app.run(debug=True)
