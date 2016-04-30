App.contact = App.cable.subscriptions.create "ContactChannel",
  connected: ->
    # Called when the subscription is ready for use on the server

  disconnected: ->
    # Called when the subscription has been terminated by the server

  received: (data) ->
    $('#contacts').append(data)

  show: (call_sign, name, location, date_time, recieved_report, given_report, state, mode, band, frequency, operator_id)->
    @perform 'show', call_sign: call_sign, name: name, location: location, date_time: date_time, recieved_report: recieved_report, given_report: given_report, state: state, mode: mode, band: band, frequency: frequency, operator_id: operator_id

$(document).on 'keypress', '[data-behavior~=contact_speaker]', (event) -> if event.keyCode is 13
	App.contact.show event.target.value
	event.target.value = ''
	event.preventDefault()