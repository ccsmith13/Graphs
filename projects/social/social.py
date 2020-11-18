import random 

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        if avg_friendships > num_users: 
            print ('Number of users must be greater than the average number of friendships')
            return
        # Add users
        for i in range(1, num_users+1):
            self.add_user(f"User {i}")
        # Create friendships
        total_friendships = avg_friendships * num_users //2
        new_friends = set()

        while len(new_friends) < total_friendships:
            first_unsub_id = random.randrange(1, num_users+1)
            second_unsub_id = random.randrange(1, num_users+1)

            #make sure these ids are not the same
            while first_unsub_id == second_unsub_id: 
                second_unsub_id = random.randrange(1, num_users+1)

            #add the friendship to new_friends set, starting with the smaller # id
            if first_unsub_id < second_unsub_id: 
                small_id = first_unsub_id
                large_id = second_unsub_id
            else: 
                large_id = first_unsub_id
                small_id = second_unsub_id
            
            new_friends.add((small_id, large_id))
        
        #now that all friendships are generated, officially add them to the self.friendships dict
        for friendship in new_friends: 
            user_1_id, user_2_id = friendship
            self.add_friendship(user_1_id, user_2_id)
        
        print(f"\nSuccessfully populated a friendship graph with {num_users} users who have an average # of {avg_friendships} friendships.\n")

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        # initialize visited dict with the starting user
        visited[user_id] = user_id

        # using BFS to find the shortest path, so we need a queue 
        # this queue will keep track of the friends not yet visited 
        q = Queue()
        # initialize the queue
        q.enqueue(user_id)

        while q.size() > 0: 
            current_friend_id = q.dequeue()
            friends_of_current_friend = self.friendships[current_friend_id]
            
            # updating the unvisited friends of friends to the queue
            for friend_id in friends_of_current_friend:
                if friend_id not in visited: 
                    q.enqueue(friend_id)
                    # make a copy of the path to this friend of friend and add the new friend in it
                    #print('visited[current_friend_id]', visited[current_friend_id])
                    if type(visited[current_friend_id]) == int: 
                        path_to_friend = [visited[current_friend_id]]
                        path_to_friend.append(friend_id)
                    else:
                        path_to_friend = list(visited[current_friend_id])
                        path_to_friend.append(friend_id)
                    # store path in visited 
                    visited[friend_id] = path_to_friend
            
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(11, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(4)
    print(connections)
