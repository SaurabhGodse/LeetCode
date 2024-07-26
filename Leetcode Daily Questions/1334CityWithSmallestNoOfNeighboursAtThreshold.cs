using System;

namespace Leetcode_Daily_Questions
{
    public class _1334CityWithSmallestNoOfNeighboursAtThreshold
    {
        /*
         * There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

           Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.

           Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.
         */
        public int FindTheCity(int n, int[][] edges, int distanceThreshold)
        {
            /*
             * Solving it using floyd-warshall algorithm
             */
            int[][] dist = new int[n][];
            for (int i = 0; i < n; i++)
            {
                dist[i] = new int[n];
                for (int j = 0; j < n; j++)
                {
                    if (i == j)
                    {
                        dist[i][j] = 0;
                    }
                    else
                    {
                        dist[i][j] = int.MaxValue;
                    }

                }
            }
            foreach (int[] edge in edges)
            {
                dist[edge[0]][edge[1]] = edge[2];
                dist[edge[1]][edge[0]] = edge[2];
            }
            for (int k = 0; k < n; k++)
            {
                for (int i = 0; i < n; i++)
                {
                    for (int j = 0; j < n; j++)
                    {
                        if (dist[i][k] == int.MaxValue || dist[k][j] == int.MaxValue)
                            continue;
                        dist[i][j] = Math.Min(dist[i][j], dist[i][k] + dist[k][j]);
                    }
                }
            }

            int city = -1;
            int belowThreshold = n;
            for (int i = 0; i < n; i++)
            {
                int count = 0;
                for (int j = 0; j < n; j++)
                {
                    if (dist[i][j] <= distanceThreshold)
                        count++;
                }
                if (count <= belowThreshold)
                {
                    city = i;
                    belowThreshold = count;
                }
            }
            return city;
        }
    }
}
