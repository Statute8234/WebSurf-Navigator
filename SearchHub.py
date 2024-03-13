import random
import webbrowser
while True:
	options = 'google, yahoo, bing, bogpile, Aoi, webcrawler, all the internet, metacrawler, random'
	print(options)
	b = input('pictuer(p) or vedio(v) or converter(c) ')
	if b == 'pictuer' or b == 'p':
		a = input('which web browser do you want to go to? ')
		if a == 'random':
			options1 = 'google','yahoo', 'bing', 'bogpile', 'Aoi', 'webcrawler', 'all the internet','metacrawler'
			a = random.choice(options1)
			print('opening',a)
		if a == 'google':
			webbrowser.open("https://www.google.com/search?q=+vault&tbm=isch&ved=2ahUKEwjZ6L_arubwAhVNEFMKHRqZDgMQ2-cCegQIABAC")
		if a == 'yahoo':
			webbrowser.open("https://images.search.yahoo.com/search/images;_ylt=AwrEzNxPwa1gU3sAInGInIlQ;_ylu=c2VjA3NlYXJjaARzbGsDYXNzaXN0;_ylc=X0kDYlZFVmRqRXdMaktCRjNQZFlLdzJaZ2p6T1RrdU5nQUFBQUJLN0hYdARfUwMxMzUxMTk1Nzg0BF9yAzIEYWN0bgNjbGsEY3NyY3B2aWQDYlZFVmRqRXdMaktCRjNQZFlLdzJaZ2p6T1RrdU5nQUFBQUJLN0hYdARmcgN5ZnAtaHJtb2IEZnIyA3NhLWdwBGdwcmlkA1hORWQxekVtUTVtVk1RN2ZDR3BhZkEEbl9yc2x0AzAEbl9zdWdnAzEwBHBvcwMxBHBxc3RyA3ZhdWx0cyBkb29yBHBxc3RybAMxMQRxc3RybAMxMARxdWVyeQN2YXVsdCUyMGRvb3IEdF9zdG1wAzE2MjE5OTk5NjEEdnRlc3RpZAM-?p=vault+door&fr=yfp-hrmob&fr2=sa-gp&ei=UTF-8&n=60&x=wrt")
		if a == 'bing':
			webbrowser.open("https://www.bing.com/images/search?q=vault+door&FORM=HDRSC2")
		if a == 'dogpile':
			webbrowser.open("https://www.dogpile.com/serp?qc=images&q=vault+doors&sc=UKmBO4ZpQwsA10")
		if a == 'Aoi':
			webbrowser.open('https://search.aol.com/aol/image;_ylt=AwrJ7FTTxa1gOaYA01J8CWVH?q=vault+door&v_t=na&s_it=searchtabs')
		if a == 'webcrawler':
			webbrowser.open("https://www.webcrawler.com/serp?qc=images&q=Vault+Door&sc=U8flZDGBkt4mHeU9SMqYrb48sEHKDS0_0aN0UIiW-hZtxK0xBUUUbZbCWQcbjV_6deeO1pZE7ltcm1uhmz3rGKgBG53ZAwYDqzRdhbNh7PNAqtoXY0Vee-wPsvDpYcPeclDLIXNzZ1_ba9eYgH_M4UB3qdf7hQ3cy8o5ify_9RX-WUfxwSTGxlHsLANhBPKXXAMVb12DQBRgS8rmASP1kkZlCu6qSOeWpdhMciDGGZq4nePgR7oe3n-ys09edaTR0uWHNYc1JytIGQVd1IKki9k1edXztqcyEP6_BKx9qXei70_Azz5roamECMtbA_r3tHuQI_9_X6Ajw5nwMlX6OKeYFuov6ggek8E8ldaHKDYGpOjq4S_3i7PJsCbWNnTf3wZwNbBPpCIV1nq1kt0B86L71RVrOoXy2NEyzaZHfpe05HKG6fR5NxowdsoRaw0u2l8h2Cf7i8B7LwPO0sIvsO4_Wce_6UUd8fa83R-jJ_R1bft2BxD5seIpJF8Mgq3P53ks3DOCWsdHMq9P0ME-Fh7jNAAQ0Gca9i2FV_B1asgAzfIuxUYacTl1TlrYvDbuSvfAb9j_3xNUT_mLQxjyANm03mSuj-NYuydlE3c7Pniy79D2OV10saOdEDGJtbfQQs8n8AW4etQ2Ijxgi9z82HzO3eieW4vlhONsLpVmL_q_MdyNGA4cYe5CgqoLGRyLlV3E3poPErtKly05e9X-tRJtlEQnvPUMyauHnzsHA09JI82uHErXBIMID8m9tQwhgzEUPAKAK1MqDhZKe3DU97p-rAIYnhanklkIrZ0Q5O-R4QQV85jToK9aE4EcbQR3HYnYSKGSUQDm2ZTNacRDk5JoI6SHGz6IEmQmacsE77NVarYROz8RrfhS4WDEkiqTn7Y2_byb99WrNny7ZWygjeHYeHc-pj_kReTyO1ow0JTpQVKjPO8X2pQ9AwAP-PDCOgebskEVx_vIKbCc6bQuvxDphJQLrh2D56JSBdF3K4ZkZDTMpCiSqgqH6SuemjXYQ_2Vco8MAJtxP6u5bdxyQynAzWOkV7WithUcIVulGAKyH7YCNIF2oVMiipDxjVmdjp7JKfTI0ekHp93fkCrE2IYRlQxTWBOtxfUk1TdJgRUWxKyuV58f9Z4-jpgUUegszhozhXK-TN4J90nH4XU7j0LczzI4J8nXkmFnQKTID_s95Ii95jN2Nn-kEiN2a_I0O0ifOuQlrboKYSAeuHpRD0-kiuaD0wzukZQD4yIIqhJpl_zeARSu8atA-EFnPltbf26w8h6sWJ1WwxkhWhtUeWWmtUVKeC_OeobWL8XY7dm577e6GL8GWgV-E1qTIsoq7VknFcH0NRoOOD6V5RUqA4cea_49Wrv_tusEL0B8BFPXQERB-5uy4pYqP5FE_e_drpE0OVz5-mNSvHPoTKBem0lwJ5Fl6oY0Teip2OcD1OwTmIa_xgbtwPp5yAz9b8NemTTwiBUm9xYOyDVliCGgn3H9Xx3dOnVkmQQKleao2-_ceDHcOF6KG60LE8DvALVNcLkJuugurgYiX2Ao646dozZzKctn_3fvO-f9svAa9uKIC3_Ado0bfjWOE0rLrjWMNPPVReTIt8kHPxJu9gLq364pNZSbDHnb7oAa7yyl79hElhJq1mDpwoZHTsqhFmrzJDKfiMaWZ2SU7nIec5H1jBuWkhtMAdKD8yKg3bWBJWjwNVCosDcHrBX7qNIMCgIIuitGkdCYZFIANihDxcJH63fc9CLHex9sM9ZBzZEa0w")
		if a == 'all the internet':
			webbrowser.open("https://www.alltheinternet.com/?q=vault+door&area=image#gsc.tab=1&gsc.q=vault%20door&gsc.page=1")
		if a == 'metacrawler':
			webbrowser.open("https://www.metacrawler.com/serp?q=Vault+Door&page=1&sc=_NbzBFYyZWXqqZV7PwA6Gcxdk1R4lCceMzYExn8iDVAS6S2amnkZP1_FWI7DQiotHxDEjny0xEBygdc2YS_Ya5yO6LZKnaiN1lz4SMrneIeqPHSUv4_kuk5IJ1oXzurhxPtcbvtWnUBQf0YDOmdtRtnpZoUoAw4pMLF4WTJgY9-eOCusKJhOrO7CiEQf6_i2newxLPH5pfVTjrt3KxIPlWE4nzuWPa1-HGiNO4zHyPZb1lNkHLCTbKafg-YRi-4ozFM5796mVf8OZJwEJMtFMbCVzjTYiM7VBd4ltdmGUji84XN7HGdMLIKnzuXxwxM8itUl4PiXykUYrSwuGsni1zzj9eLUs_NBPg-EuQa7jmBhHY-MQ6LCdaKdZyOGUqZkR7anaokWRYtY1IrNlVdkJSelEyyKyne3dVZZps85_8HkaIAcb8tV7H9nCvd76n3vgeOitflQ3iJkcNCUkoQ4iHF57A3DZthUWiqf5Q_wPgdgRnsgd158HjhGKmBlyNBMHssFYAnGpKdE81HgEE8YuWtl_nRttDo8MUmN_N5PcidkGznlt-lGQNICo6LKiqu6AqNcyvUb6AQQJs18OVwfyZKYLIpmVDSv5kMn2Kw7Z91mKtkhSPMgT69zeKV1xEXnMrmvwkpt18YtOgQ2K8rEWfBej74tBKIw8axI-ZEWxTyYn6cFv2SEfI3sQGoiet_ZL9QOL3XP2ZIiQgkJThxD4zcoIlNrXv7qNf8xi6HsF0l_IHVQfvzSUb_Nsfyfr-VHBUTQ6IWK89niUQx8oCitrFgQuHryRo__A1YBRx5EkX-mRlTn1MSC8Ce8q84Z_3m4dmR194DHZ4xqtmCsUXY4iwQfGXw1-8EgF1wWMS0qFUAwzpqrHRcR9dFF5xldjDYsw7gDNbRfT6PlP-qGZZOqAkCtqMl0Qu6Xef_5CPvaAnLU8ylXrqh6Ct_jEeXzgJhGjkn6guqFZSRS7SptQG9hdfKb3piZ_y8a-Ech7E9HG40DY5rJj2rkuD4jQhJMz_c2OFNLpITos2ud1F_qU_EFLeHBUzgb7qJc8MSQ_WbhHs1dh5EMbsZCvbgxVN-50ItEc9-UuSeLelNkbVlGpMZHZjzdgsJ9wOwuXfbPhfWFIlhtyjxP0TTTp0ZxZvF3FnPH8ON4v0maOohgbtoXm4xiA788_lYivgvRGDUwH_pgx85WyEZualVMT7O91y1x8Ds75dJTo7yWnUxKH03xFaL_3LN-kGTeccGGZQX2aUhrbCzZ4H4WDDe6odLVt9r5TS9QyD37AG5aQQeQwh5jBENm6QGjDK01754uqAGb-3iy7Q-W5dMtZH2EvIFul1zWR3DpR2T14iPr53kbTICyb6oDU7IAOKqKscd4sSif2tiCCxcJfQV-rS8HIMZKfv7sLmU5_u1nmiHRVWVdelELC8d1HGHI896gW-5FFmNnyJ9OFYYQkBbqNA1VBEGMb4ghUjncnwDA1x_0Bcb94v6mVeEE7vC3_LOWWZLqfjbFsl6og379Z6-uhIPZR-X09NSVVHODxuhP6qrL7cZYxeCqXI34ZD6dx2Go-Jw83Ayt2n7RQ-P750SPNDP18qXjT5TUUzFDZeZgB2Nkih-IC3bhwd--7oSLlBnSyx6pUi7WP3gngFKS-gF4fZvWvrQwIFKDYnZe3IedLxgiJVJmGuA8bejQO5HJR7wI-VVkDb8Y2LJ7bgj-feGeq329Xb3iu04FoLK0edNgLA4gUffZiqY8Jkd2D-19l-iys010WWcly3zkwZKZN8iLAfvBpuKCqKmeh0eHfRLEhKg2r6zTUW1bWIVkX_Q_OWP-Scc6w-_86FeOaJiyCQeNVTWUWVnvbLejp62LUAfE4ThfWgHxaFLUAZgiomX2wIpugaI1F2ISic2tO_6zbw")
	if b == 'vedio':
		webbrowser.open("https://m.youtube.com/results?sp=mAEA&search_query=Vault+Door")
	if b == 'converter' or b == 'c':
		webbrowser.open("https://ytmp3.cc/youtube-to-mp3/")
	print('')
