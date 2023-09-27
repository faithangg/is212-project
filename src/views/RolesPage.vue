// Inside your Vue component
<template>
    <div>
        <!-- Display role listings using the RoleListings component -->
        <RoleListings :roleListings="roleListings" />
    </div>
</template>

<script>
import axios from 'axios';
import RoleListings from '../components/RoleListings.vue'; // Import the RoleListings component

export default {
    data() {
        return {
            roleListings: [], // Initialize as an empty array
        };
    },
    mounted() {
        // Fetch role listings from the API
        axios.get('http://127.0.0.1:5000/hr/role_listings')
            .then((response) => {
                console.log(response.data.data);
                // this.roleListings = response.data.data.role_listing; // Set the retrieved data to roleListings
                this.roleListings = [
                    {
                        "category": "Administration and Support",
                        "deadline": "2023-09-30",
                        "department": "HR",
                        "listing_id": 1,
                        "role_name": "Manager",
                        "skills_required": [
                            "Python",
                            "SQL"
                        ]
                    },
                    {
                        "category": "Engineering",
                        "deadline": "2023-10-15",
                        "department": "IT",
                        "listing_id": 2,
                        "role_name": "Engineer",
                        "skills_required": [
                            "Python"
                        ]
                    }

                ]
            })
            .catch((error) => {
                console.error('Error fetching role listings:', error);
            });

    },

    components: {
        RoleListings, // Register the RoleListings component
    },


};
</script>
