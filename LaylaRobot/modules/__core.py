from LaylaRobot import telethn as tbot
from LaylaRobot.events import register
import os
import asyncio
import os
import time
from datetime import datetime
from LaylaRobot import OWNER_ID, DEV_USERS
from LaylaRobot import TEMP_DOWNLOAD_DIRECTORY as path
from LaylaRobot import TEMP_DOWNLOAD_DIRECTORY
from datetime import datetime
water = './LaylaRobot/resources/hero.png'
client = tbot

@register(pattern=r"^/send ?(.*)")
async def Prof(event):
    if event.sender_id == OWNER_ID or event.sender_id == DEV_USERS:
        pass
    else:
        return
    thumb = water
    message_id = event.message.id
    input_str = event.pattern_match.group(1)
    the_plugin_file = "./LaylaRobot/modules/{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
     message_id = event.message.id
     await event.client.send_file(
             event.chat_id,
             the_plugin_file,
             force_document=True,
             allow_cache=False,
             thumb=thumb,
             reply_to=message_id,
         )
    else:
        await event.reply("No File Found!")



                    ),
                )
            else:
                os.remove(downloaded_file_name)
                k = await event.reply("**Error!**\n⚠️Cannot Install! \n📂 File not supported \n Or Pre Installed Maybe..😁",
                )
                await asyncio.sleep(2)
                await k.delete()
        except Exception as e:  # pylint:disable=C0103,W0703
            j = await event.reply(str(e))
            await asyncio.sleep(3)
            await j.delete()
            os.remove(downloaded_file_name)
    await asyncio.sleep(3)
    await event.delete()
