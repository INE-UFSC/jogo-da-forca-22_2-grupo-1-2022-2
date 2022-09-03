#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Description:

"""
modules = True

try:
    import aiohttp
    import asyncio
except:
    print("Not using aiohttp and asyncio modules to randomize the word")
    modules = False

class Word:

    def __init__(self):

        self.word = ""

        if modules:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self.get_random_word())
        else:
            get_word_from_list()

    async def get_random_word(self):

        async with aiohttp.ClientSession() as session:
            async with session.get('https://www.palavrasque.com/palavra-aleatoria.php?Submit=Nova+palavra') as response:

                # print("Status:", response.status)
                # print("Content-type:", response.headers['content-type'])

                html = await response.text()
                html_s1 = html.split("font data=\"palavra\" size=\"6\" /><b>", 1)[1] # Split the part before the random word
                html_s2 = html_s1.split("</b></fo")[0] # Split the part after the random word
                self.word = html_s2

    def get_word_from_list(self):
        with open("Lista-de-Palavras.txt", "r") as f:
            text_list = f.readlines()
