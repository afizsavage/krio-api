class RollbackColumnNameChange < ActiveRecord::Migration[7.0]
  def change
    rename_column :words, :author_id, :user_id
    rename_column :definations, :reviewer_id, :user_id
  end
end
