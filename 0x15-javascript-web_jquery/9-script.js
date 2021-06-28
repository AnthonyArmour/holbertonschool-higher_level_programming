#!/usr/bin/node

$.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: function(data) {
    //   the query below shows results key which holds list of resluts
      $('#hello').append('<p>'+ data.hello+ '</p>');
    }
  });
  