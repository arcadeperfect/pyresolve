class Mother:
    def __init__(self, resolve):
        self.resolve = resolve
        self.project = resolve.GetProjectManager().GetCurrentProject()
        self.timeline = self.project.GetCurrentTimeline()
        self.media_pool = self.project.GetMediaPool()
        self.media_storage = resolve.GetMediaStorage()
        self.root_bin = self.media_pool.GetRootFolder()

    def add_bin(self, name, parent = None):
        if parent is None:
            parent = self.root_bin
        existing_bins = {bin.GetName():bin for bin in parent.GetSubFolderList()}
        if name in existing_bins.keys():
            print(f"Bin {name} already exists")
            return existing_bins[name]
        return self.media_pool.AddSubFolder(parent, name)

    def add_bins(self, names, parent = None):
        if parent is None:
            parent = self.root_bin
        # existing_bins = [bin.GetName() for bin in parent.GetSubFolderList()]

        existing_bins = {bin.GetName():bin for bin in parent.GetSubFolderList()}

        bins = []
        for name in names:
            if name in existing_bins.keys():
                print(f"Bin {name} already exists")
                bins.append(existing_bins[name])
                continue
            bin = self.media_pool.AddSubFolder(parent, name)
            bins.append(bin)

        return bins
