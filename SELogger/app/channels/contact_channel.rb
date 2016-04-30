# Be sure to restart your server when you modify this file. Action Cable runs in a loop that does not support auto reloading.
class ContactChannel < ApplicationCable::Channel
  def subscribed
    stream_from "contact_channel"
  end

  def unsubscribed
    # Any cleanup needed when channel is unsubscribed
  end

  def show(data)
  	Contact.create(call_sign: data["call_sign"], name: data["name"])
  end
end
