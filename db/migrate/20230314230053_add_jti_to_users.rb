class AddJtiToUsers < ActiveRecord::Migration[7.0]
  def change
    User.all.each { |user| user.update_column(:jti, SecureRandom.uuid) }
    change_column_null :users, :jti, false
  end
end
