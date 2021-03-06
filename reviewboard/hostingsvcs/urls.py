from __future__ import unicode_literals

from django.conf.urls import include, patterns, url
from djblets.urls.resolvers import DynamicURLResolver


dynamic_urls = DynamicURLResolver()


urlpatterns = patterns(
    '',

    (r'^repos/(?P<repo_id>\d+)/', include(patterns('', dynamic_urls))),
)
