import os
import re
from PIL import Image, ImageDraw, ImageFont
import random

# Create directories for team logos if they don't exist
teams_dirs = [
    'football/painel/static/img/teams',
    'football/painel/central/static/img/teams'
]

for dir_path in teams_dirs:
    os.makedirs(dir_path, exist_ok=True)

# Updated list of team image URLs from error logs
team_urls = [
    # Original team logos
    "andorra-inter-club-descaldes.png",
    "andorra-fc-ordino.png",
    "andorra-don-denis-fc-santa-coloma.png",
    "england-brentford-fc.png",
    "england-manchester-united-fc.png",
    "armenia-fk-van.png",
    "england-brighton-hove-albion-fc.png",
    "andorra-m-perruquers-atletic-club-descaldes.png",
    "armenia-fc-artsakh.png",
    "england-west-ham-united-fc.png",
    "brazil-vilavelhense.png",
    "england-newcastle-united-fc.png",
    "england-tottenham-hotspur-fc.png",
    "brazil-sport-clube-brasil-capixaba.png",
    "andorra-rangers-fc-andorra.png",
    "andorra-tic-tapa-ue-santa-coloma.png",
    "angola-gd-sagrada-esperanca.png",
    "angola-cd-sao-salvador-do-kongo.png",
    "angola-academica-petroleos-do-lobito.png",
    "angola-atletico-petroleos-luanda.png",
    "angola-luanda-city-fc.png",
    "angola-cd-da-huila.png",
    "angola-fc-onze-bravos-do-maquis.png",
    "armenia-pyunik-fc.png",
    "angola-cd-primeiro-de-agosto.png",
    "angola-banaki-kentronakan-marzakan-akumb.png",
    "armenia-banaki-kentronakan-marzakan-akumb.png",
    "england-chelsea-fc.png",
    "andorra-cf-esperanca-dandorra.png",
    "england-liverpool-fc.png",
    "argentina-gimnasia-y-esgrima-la-plata.png",
    "argentina-ca-platense.png",
    "andorra-deportivo-massana.png",
    "argentina-ca-san-martin-de-san-juan.png",
    "argentina-ca-aldosivi.png",
    "brazil-goiatuba-esporte-clube.png",
    "brazil-itabirito-fc.png",
    "brazil-se-palmeiras.png",
    "brazil-cr-vasco-da-gama.png",
    "brazil-gremio-fb-porto-alegrense.png",
    "brazil-santos-fc-sao-paulo.png",
    "brazil-ac-goianiense.png",
    "brazil-gremio-novorizontino.png",
    "brazil-parnahyba-sc.png",
    "brazil-associacao-esportiva-de-altos.png",
    "brazil-maracana-ec.png",
    "brazil-associacao-desportiva-iguatu.png",
    "brazil-america-fc-rio-grande-do-norte.png",
    "brazil-ad-jequie.png",
    "brazil-central-sc.png",
    "brazil-treze-fc.png",
    "brazil-sousa-ec.png",
    "brazil-uniao-atletica-carmolandense.png",
    "brazil-sd-juazeirense.png",
    "brazil-goianesia-ec.png",
    "brazil-barcelona-de-ilheus.png",
    "brazil-aa-aparecidense.png",
    "brazil-ypiranga-erechim.png",
    "brazil-cs-alagoano.png",
    "brazil-retro-fc-brasil.png",
    "brazil-floresta-ec.png",
    "brazil-horizonte-fc.png",
    "brazil-ferroviario-ac-fortaleza.png",
    "argentina-ca-tigre.png",
    "argentina-ca-boca-juniors.png",
    "brazil-associacao-portuguesa-de-desportos.png",
    "brazil-esporte-clube-agua-santa.png",
    "brazil-cruzeiro-ec.png",
    "brazil-ca-paranaense.png",
    "brazil-cr-flamengo.png",
    "brazil-clube-nautico-capibaribe.png",
    "brazil-chapecoense-af.png",
    "brazil-botafogo-fc-ribeirao-preto.png",
    "brazil-criciuma-ec.png",
    "brazil-guarani-fc-de-campinas.png",
    "brazil-brusque-fc.png",
    "brazil-botafogo-fc-joao-pessoa.png",
    "brazil-independencia-futebol-clube.png",
    "brazil-sc-humaita.png",
    "argentina-ca-river-plate.png",
    "argentina-club-atletico-velez-sarsfield.png",
    "brazil-operario-ferroviario-ec.png",
    "brazil-america-fc-minas-gerais.png",
    
    # New team logos from console errors
    "england-afc-fylde.png",
    "england-barnet-fc.png",
    "england-aldershot-town-fc.png",
    "england-altrincham-fc.png",
    "england-braintree-town-fc.png",
    "england-rochdale-afc.png",
    "england-tamworth-fc.png",
    "england-yeovil-town-fc.png",
    "england-york-city-fc.png",
    "england-gateshead-fc.png",
    "england-eastleigh-fc.png",
    "england-hartlepool-united-fc.png",
    "england-southend-united-fc.png",
    "england-forest-green-rovers-fc.png",
    "england-ebbsfleet-united-fc.png",
    "england-maidenhead-united-fc.png",
    "england-boston-united-fc.png",
    "england-nottingham-forest-fc.png",
    "england-fc-halifax-town.png",
    "england-solihull-moors-fc.png",
    "england-oldham-athletic-afc.png",
    "england-crystal-palace-fc.png",
    "england-dagenham-redbridge-fc.png",
    "england-wealdstone-fc.png",
    "england-sutton-united-fc.png",
    "england-woking-fc.png",
    "brazil-mirassol-futebol-clube.png",
    "brazil-clube-atletico-bragantino.png",
    "brazil-goias-ec.png",
    "brazil-avai-fc.png",
    "brazil-londrina-ec.png",
    "brazil-sao-bernardo-fc.png",
    "brazil-figueirense-fc.png",
    "brazil-sociedade-esportiva-e-recreativa-caxias-do-sul.png",
    "brazil-ec-juventude.png",
    "brazil-ca-mineiro.png"
]

def generate_team_logo(team_filename):
    """Generate a placeholder logo for the team"""
    # Parse team name
    country, team = team_filename.replace('.png', '').split('-', 1)
    team_name = team.replace('-', ' ').title()
    country_name = country.title()
    
    # Generate random team color (biased toward common team colors)
    colors = [
        (0, 0, 255),  # Blue
        (255, 0, 0),  # Red
        (0, 0, 0),    # Black
        (255, 255, 0), # Yellow
        (0, 255, 0),  # Green
        (128, 0, 128), # Purple
        (165, 42, 42), # Brown
        (255, 165, 0), # Orange
    ]
    
    color = random.choice(colors)
    
    # Create image with background color
    img = Image.new('RGB', (200, 200), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Draw colored circle
    draw.ellipse((30, 30, 170, 170), fill=color, outline=(0, 0, 0))
    
    # Add text (team initials)
    initials = ''.join([word[0] for word in team_name.split() if word and not word.startswith('(') and word not in ['FC', 'AC', 'SC', 'EC']])
    if not initials and team_name:
        initials = team_name[0]
    
    # Draw text
    try:
        font = ImageFont.truetype("arial.ttf", 60)
    except:
        font = ImageFont.load_default()
    
    draw.text((100, 100), initials, fill=(255, 255, 255), font=font, anchor="mm")
    
    # Draw country at bottom
    try:
        small_font = ImageFont.truetype("arial.ttf", 16)
    except:
        small_font = ImageFont.load_default()
    
    draw.text((100, 180), country_name, fill=(0, 0, 0), font=small_font, anchor="mm")
    
    # Save the image to both locations
    img_paths = []
    for dir_path in teams_dirs:
        img_path = os.path.join(dir_path, team_filename)
        img.save(img_path)
        img_paths.append(img_path)
    
    return img_paths

# Generate placeholder logos for each team
for team_filename in team_urls:
    try:
        img_paths = generate_team_logo(team_filename)
        for path in img_paths:
            print(f"Generated logo for {team_filename} at {path}")
    except Exception as e:
        print(f"Error generating logo for {team_filename}: {e}")

print(f"Generated {len(team_urls)} team logos in both directories") 