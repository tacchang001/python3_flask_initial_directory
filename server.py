'''サーバ起動スクリプト'''
from app import sample

if __name__ == '__main__':
    sample.run(host='127.0.0.1', port=5000, debug=True)