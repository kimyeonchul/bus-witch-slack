from slack_sdk import WebClient
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import config

app = App(token=config.SLACK_TOKEN)
slack_client = WebClient(token=config.SLACK_TOKEN)

@app.event('message')
def handle_massage(event, say):
    user = event['user']
    text = event['text']
    split_data = text.strip().split(',')
    result = []
    for item in split_data:
      if item.isdigit():
        result.append({"routeNum": int(item)})
      elif item.endswith('구'):
        result.append({"borough": item})
      else :
        result.append({"category":item})
    url_parameter_string = "&".join([f"p.{list(data.keys())[0]}={list(data.values())[0]}" for data in result])
    quicksight_url = config.URL + url_parameter_string
    quicksight_embed_url = f'{quicksight_url}&embed=true'
    print(quicksight_embed_url)
    #Slack 메시지에 대시보드 URL과 이미지 추가
    message = {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f'{quicksight_embed_url}'
                },
                "accessory": {
                    "type": "image",
                    "image_url": "URL_TO_YOUR_THUMBNAIL_IMAGE",
                    "alt_text": "QuickSight Dashboard"
                }
            }
        ]
    }

    # Slack 메시지 전송
    slack_client.chat_postMessage(channel=event['channel'], blocks=message['blocks'])

if __name__ == "__main__":
    SocketModeHandler(app,config.APP_TOKEN).start()
