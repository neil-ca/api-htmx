import pika
import json


def upload(f, fs, channel, access):
    try:
        fid = fs.put(f)
    except Exception:
        return "internal server error", 500

    message = {
        "video_fid": str(fid),
        "mp3_fid": None,
        "username": access["username"],
    }

    try:
        channel.basic_publish(
            exchange="",
            routing_key="video",
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE1
            ),
        )
    except Exception:
        fs.delete(fid)
        return "internl server error", 500
