class CreateOperators < ActiveRecord::Migration[5.0]
  def change
    create_table :operators do |t|
      t.string :name
      t.string :call_sign
      t.string :location
      t.belongs_to :event, foreign_key: true

      t.timestamps
    end

    create_table :contacts do |t|
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
      t.belongs_to :operator, foreign_key: true

      t.timestamps
    end
  end
end
