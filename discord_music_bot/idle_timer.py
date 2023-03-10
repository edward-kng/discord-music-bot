import asyncio


async def start_idle_timer(sessions, guild):
    session = sessions[guild]

    while session.is_active():
        idle_secs = 0

        await asyncio.sleep(0.1)

        while not session.is_playing() and session.is_active():
            await asyncio.sleep(1)

            idle_secs += 1

            if idle_secs >= 300:
                await session.quit()

                sessions.pop(guild)
