class CreateSpecialEventStations < ActiveRecord::Migration[5.0]
  def change
    create_table :special_event_stations do |t|
      t.string :call_sign

      t.timestamps
    end

    create_table :operators do |t|
    	t.belongs_to :special_event_station
      t.string :call_sign
      t.string :name
      t.string :location

      t.timestamps
    end

    create_table :contacts do |t|
    	t.belongs_to :operator
      t.string :call_sign
      t.string :name
      t.string :location
      t.datetime :date_time
      t.integer :recieved_report
      t.integer :given_report
      t.string :state
      t.string :mode
      t.string :band
      t.float :frequency

      t.timestamps
    end
  end
end
