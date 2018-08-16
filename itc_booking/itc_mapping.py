# containing the common mapping between comment and ITC tag with type
tag_mapping = {
  'mail': ('Work', 'nevismeta/main'),
  'trade union': ('Admin Various', None),
  'daily standup': ('Internal Meeting', 'nevismeta/various'),
  'nevismeta': ('Work', 'nevismeta/main')
}

template_mapping = {
  'mail': 'mail.json',
  'nevismeta': 'nevismeta.json',
  'trade union': 'tradeunion.json',
  'adpropositum': 'adpropositum.json',
  'daily standup': 'internal-meeting.json',
  'town hall meeting': 'admin-various.json',
  'vnpropositum': 'admin-various.json',
  'andocnoitech': 'internal-edu.json'
}
