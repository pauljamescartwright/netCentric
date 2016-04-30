class ContactBroadcastJob < ApplicationJob
  queue_as :default

  def perform(contact)
  	ActionCable.server.broadcast 'contact_channel', message: render_contact(contact)
  end

  private
  	def render_contact(contact)
  		ApplicationController.renderer.render(partial: 'contacts/contact', locals: { contact: contact})
  	end
end
