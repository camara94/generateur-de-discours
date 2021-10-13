from scrapy import Request, Spider
from ..items import DiscoursGouvFrItem, UrlPattern


class SpiderDiscours(Spider):
    name = "discours"
    urls = [
        "https://www.gouvernement.fr/partage/12491-institut-des-hautes-etudes-de-defense-nationale-ihedn",
        "https://www.gouvernement.fr/partage/12489-numerique-educatif-le-premier-ministre-dresse-le-bilan-des-enseignements-de-la-crise-et-presente-des",
        "https://www.gouvernement.fr/partage/12488-le-numerique-au-service-de-l-innovation-pedagogique-et-de-l-egalite-des-chances",
        "https://www.gouvernement.fr/partage/12483-resultats-de-l-appel-a-projets-transports-collectifs-en-site-propre-et-poles-d-echanges-multimodaux",
        "https://www.gouvernement.fr/partage/12485-resultats-de-l-appel-a-projets-transports-collectifs-en-site-propre-tourcoing",
        "https://www.gouvernement.fr/partage/12480-signature-d-un-contrat-de-securite-integree-entre-l-etat-et-les-villes-de-rennes-et-de-saint-jacques",
        "https://www.gouvernement.fr/partage/12478-discours-de-cloture-de-jean-castex-au-17eme-congres-de-regions-de-france-a-montpellier",
        "https://www.gouvernement.fr/partage/12474-discours-de-jean-castex-au-congres-hlm-de-l-ush-de-bordeaux",
        "https://www.gouvernement.fr/partage/12473-congres-hlm",
        "https://www.gouvernement.fr/partage/12470-plan-de-reduction-des-tensions-de-recrutement",
        "https://www.gouvernement.fr/partage/12467-3eme-comite-interministeriel-aux-ruralites",
        "https://www.gouvernement.fr/partage/12465-plfss-2022-l-etat-s-engage-pour-le-grand-age-et-l-autonomie",
        "https://www.gouvernement.fr/partage/12461-remise-du-rapport-de-la-commission-pour-la-relance-durable-de-la-construction-de-logements",
        "https://www.gouvernement.fr/partage/12458-experimentation-de-la-recentralisation-du-financement-du-rsa-en-seine-saint-denis",
        "https://www.gouvernement.fr/partage/12455-journees-europeennes-du-patrimoine-2021",
        "https://www.gouvernement.fr/partage/12448-500-000eme-maprimerenov-discours-du-premier-ministre-jean-castex-a-chillu-mazarin-le-16-septembre",
        "https://www.gouvernement.fr/partage/12446-rencontre-avec-les-acteurs-de-l-enseignement-des-langues-regionales",
        "https://www.gouvernement.fr/partage/12445-remise-du-rapport-d-enquete-administrative-concernant-edouard-levrault",
        "https://www.gouvernement.fr/partage/12443-session-pleniere-de-rentree-du-conseil-economique-social-et-environnemental",
        "https://www.gouvernement.fr/partage/12436-journees-nationales-de-france-urbaine-a-nantes",
        "https://www.gouvernement.fr/partage/12433-remise-du-rapport-pour-un-usage-responsable-et-acceptable-par-la-societe-des-technologies-de",
        "https://www.gouvernement.fr/partage/12428-1-an-de-france-relance",
        "https://www.gouvernement.fr/partage/12432-discours-du-premier-ministre-jean-castex-compte-rendu-du-conseil-des-ministres-et-du-seminaire",
        "https://www.gouvernement.fr/partage/12426-discours-du-premier-ministre-jean-castex-conseil-national-de-l-industrie",
        "https://www.gouvernement.fr/partage/12412-commemoration-de-l-attentat-contre-des-humanitaires-francais-au-niger",
        "https://www.gouvernement.fr/partage/12411-pass-sanitaire-pour-rester-ensemble-face-au-virus"
    ]

    def start_requests(self):
        for url in self.urls:
            yield Request(url=url, callback=self.parse_discours)

    def parse_discours(self, response):
        divs = response.css('div.rf-grid-row')
        for div in divs:
            titre = div.css('h1.rf-mb-3w::text').extract_first()
            date = div.css('span.rf-b-contenu-date::text').extract_first()
            discours = div.css(
                'div.field-items div.field-item p::text').extract_first()
            if discours != None:
                item = DiscoursGouvFrItem()
                item['titre'] = titre
                item['date'] = date
                item['discours'] = discours
                yield item
            else:
                pass
