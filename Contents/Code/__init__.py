#Plex Theme Music
THEME_URL = 'http://tvthemes.plexapp.com/%s.mp3'

def Start():
  HTTP.CacheTime = CACHE_1DAY
  
class PlexThemeMusicAgent(Agent.TV_Shows):
  name = 'Plex Theme Music'
  languages = [Locale.Language.NoLanguage]
  primary_provider = False
  contributes_to = ['com.plexapp.agents.thetvdb']

  def search(self, results, media, lang):
    results.Append(
      MetadataSearchResult(
        id    = media.primary_metadata.id,
        score = 100
      )    
    )

  def update(self, metadata, media, lang):
    if THEME_URL % metadata.id not in metadata.themes:
      try:
        metadata.themes[THEME_URL % metadata.id] = Proxy.Media(HTTP.Request(THEME_URL % metadata.id))
      except:
        pass