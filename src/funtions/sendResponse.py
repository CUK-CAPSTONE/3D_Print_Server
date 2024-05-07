import requests

def send_response(payment_id, status):
    url = f'https://capstone.hyunn.site/api/printer/commit?payment_id={payment_id}'
    headers = {
        'accept': '/',
        'x-api-key': 'wkflsrhql2024'
    }
    
    if status == 'success':
        response_data = {
            'code': '00',
            'msg': 'success',
            'data': '프린팅이 성공적으로 완료되었습니다.'
        }
    else:
        response_data = {
            'code': '99',  # 오류 상황에서는 '99'와 같은 코드 값을 사용합니다.
            'msg': 'fail',
            'data': '프린팅 중 오류가 발생했습니다.'
        }
    
    try:
        response = requests.post(url, headers=headers, json=response_data)
        response.raise_for_status()  # 요청이 실패하면 예외를 발생시킵니다.
        print('응답을 성공적으로 전송했습니다.')
    except requests.exceptions.RequestException as e:
        print(f'응답 전송 중 오류가 발생했습니다: {str(e)}')
