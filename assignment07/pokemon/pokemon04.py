import aiofiles
import asyncio
import json
from pathlib import Path

pokemonapi_directory = r'C:\Users\ballg\Desktop\Async\asyncioclass67\assignment07\pokemon\pokemonapi'
pokemonmove_directory = r'C:\Users\ballg\Desktop\Async\asyncioclass67\assignment07\pokemon\pokemonmove'

async def process_file(file_path):
    async with aiofiles.open(file_path, mode='r') as f:
        contents = await f.read()

    pokemon = json.loads(contents)
    name = pokemon['name']
    moves = [move['move']['name'] for move in pokemon['moves']]
    
    output_file = Path(pokemonmove_directory) / f'{name}_moves.txt'
    async with aiofiles.open(output_file, mode='w') as f:
        await f.write('\n'.join(moves))
    
async def main():
    pathlist = Path(pokemonapi_directory).glob('*.json')

    # Iterate through all json files in the directory.
    tasks = [process_file(path) for path in pathlist]
    await asyncio.gather(*tasks)

    print("Processing complete.")
        

asyncio.run(main())
