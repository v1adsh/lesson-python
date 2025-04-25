import python_weather
import asyncio
import os

async def getweather() -> None:
    async with python_weather.Client(unit=python_weather.IMPERIAL, locale = python_weather.Locale.RUSSIAN) as client:

        weather = await client.get('Томск')
        celsius = (weather.temperature - 32) / 1.8

        print(str(celsius) + 'градусов по Цельсию')
        print(weather.region)
        print(weather.country)
        print(weather.wind_speed)

        # for daily in weather:
        #     print(daily)

            # for hourly in daily:
                # print(f' --> {hourly!r}')

if __name__ == '__main__':
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(getweather())
