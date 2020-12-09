import matplotlib.pyplot as plt
from content_based_filtering.helpers.movies import get_movie_id, get_movie_name, get_movie_year

class Recommendation:
    
    similarity_matrix = None;
    movies_dataframe = None;
    ratings_dataframe = None;
    users_dataframe = None;
    
    def load_all_datasets(path_to_all_datasets):
    
        all_dataframes = []

        try:
            for path in path_to_all_datasets:
                all_dataframes.append(pd.read_csv(path))
                
            return all_dataframes
        except:
            return None
        
    

    def visualize_user_dataset():
            fig, axes = plt.subplots(1,2)
            axes[0].boxplot(this.users_dataframe["age"])
            axes[0].set_title("Age boxplot distribution")

            axes[1].hist(this.users_dataframe["occupation"])
            axes[1].set_title("Occupation distribution")

            plt.tight_layout()
    
    def visualize_movie_dataset(movie_dataset, not_genre_columns):
    
        this.movies_dataframe.sum()[list(set(movie_dataset.columns.to_list())-set(not_genre_columns))].plot(kind="bar")
    
    def generate_feature_frame(ratings,users,movies):

        ratings_users = pd.merge(left=this.ratings_dataframe,right=this.users_dataframe,how='inner',on='user_id')
        ratings_users_movies = pd.merge(left=ratings_users,right=this.movies_dataframe,how='inner',on='movie_id')
        assert ratings_users_movies.shape[0] == ratings.shape[0]
        ratings_users_movies_cleaned = ratings_users_movies.drop(columns=["movie_id","rating","zip_code","title","year"])
        ratings_users_movies_cleaned = ratings_users_movies_cleaned.groupby(['user_id','gender','age','occupation']).agg("sum").reset_index()
        ratings_users_movies_cleaned = pd.get_dummies(data=ratings_users_movies_cleaned,columns=["occupation"],prefix=
                                                      ["occupation"],drop_first=False)
        ratings_users_movies_cleaned = pd.get_dummies(data=ratings_users_movies_cleaned,columns=["gender"],prefix=["gender"],drop_first=True)
        assert ratings_users_movies_cleaned.shape[0] == users.shape[0]
        return ratings_users_movies_cleaned,list(set(features_matrix.columns)-set(["user_id"]))
    
    def _get_similarity_matrix(matrix):
        return matrix.values.dot(matrix.values.T)
    
    def _get_most_similar_users_id(similarity_matrix, user_id,top=10):
        best_users = list(similarity_matrix[user_id].argsort()[-top:])
        if user_id in best_users:
            best_users.remove(user_id)
        return best_users
    
    def get_best_rated_movies_by_user(user_id_list,ratings,movies,top_k):
    
        temp = pd.concat([ratings.loc[ratings["user_id"]==user_id].sort_values(by='rating', ascending=False) for user_id in 
                          user_id_list],ignore_index=True)
        return temp.sort_values(by='rating', ascending=False)["movie_id"].unique()[:top_k] 
    
    

    def get_recommendations(similarity_matrix,user_id,num_user_to_consider,num_of_movies):

        best_movies =
        get_best_rated_movies_by_user(get_most_similar_users_id(similarity_matrix,user_id,num_user_to_consider),ratings,movies,num_of_movies)
        most_similars = []
        
        for top_movie in best_movies:
            most_similars.append((top_movie,get_movie_name(movies, top_movie), get_movie_year(movies, top_movie)))
        
        return pd.DataFrame(most_similars, columns=["movie_id","movie_name","movie_year"])
