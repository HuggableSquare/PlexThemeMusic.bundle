#Plex Theme Music
THEME_URL = 'http://tvthemes.plexapp.com/%s.mp3'

def Start():
  HTTP.CacheTime = CACHE_1DAY

class PlexThemeMusicAgent(Agent.TV_Shows):
  name = 'Plex Theme Music DVD Order'
  languages = [Locale.Language.NoLanguage]
  primary_provider = False
  contributes_to = [
    'com.plexapp.agents.thetvdbdvdorder'
  ]

  def search(self, results, media, lang):
    if media.primary_agent == 'com.plexapp.agents.thetvdbdvdorder':
      results.Append(MetadataSearchResult(
        id = media.primary_metadata.id,
        score = 100
      ))

  def update(self, metadata, media, lang):
    if THEME_URL % metadata.id not in metadata.themes:
      try:
        metadata.themes[THEME_URL % metadata.id] = Proxy.Media(HTTP.Request(THEME_URL % metadata.id))
      except:
        pass
