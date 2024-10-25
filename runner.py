import uvicorn

if __name__ == '__main__':
    # lunch this file if you're working from windows, because its terminal is shit as fuck
    uvicorn.run('app.main:app', host='127.0.0.1', port=8000, reload=True)